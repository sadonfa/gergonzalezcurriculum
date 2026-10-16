import requests
import hashlib
import time
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string
from .serializers import SolicitudContactoSerializer
from .models import TransaccionPago

@api_view(['POST'])
@permission_classes([AllowAny])
def registrar_contacto(request):
    serializer = SolicitudContactoSerializer(data=request.data)
    if serializer.is_valid():
        solicitud = serializer.save()

        # Enviar notificación a tu casilla corporativa
        try:
            asunto = f"Nueva solicitud web: {solicitud.servicio}"
            contenido = (
                f"Has recibido un nuevo mensaje desde el portal GEGOVA:\n\n"
                f"• Nombre / Empresa: {solicitud.nombre}\n"
                f"• Correo corporativo: {solicitud.email}\n"
                f"• Servicio de interés: {solicitud.servicio}\n"
                f"• Mensaje:\n{solicitud.mensaje or 'Sin mensaje adicional'}\n\n"
                f"Fecha: {solicitud.creado_en.strftime('%Y-%m-%d %H:%M')}"
            )
            
            send_mail(
                subject=asunto,
                message=contenido,
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=['dirsistemas@gegova.com.co'],  # <-- Aquí colocas tu correo destinatario
                fail_silently=False,
            )
        except Exception as e:
            print("Error al despachar el correo:", e)

        return Response(
            {"mensaje": "Solicitud recibida exitosamente."}, 
            status=status.HTTP_201_CREATED
        )
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([AllowAny])
def procesar_pago_wompi(request):
    token_tarjeta = request.data.get('token')
    precio = request.data.get('precio')
    producto_id = request.data.get('producto_id')
    producto_titulo = request.data.get('producto_titulo', producto_id)
    
    nombre_cliente = request.data.get('nombre_cliente', 'Cliente GEGOVA')
    email_cliente = request.data.get('email_cliente')
    telefono_cliente = request.data.get('telefono_cliente', 'No especificado')

    if not token_tarjeta or not precio or not email_cliente:
        return Response({"error": "Faltan datos requeridos (token, precio o correo)."}, status=status.HTTP_400_BAD_REQUEST)

    monto_centavos = int(precio) * 100 
    moneda = "COP"

    tiempo_actual = int(time.time() * 1000)
    referencia_unica = f"GEGOVA_{producto_id}_{tiempo_actual}"

    secreto_integridad = getattr(settings, 'WOMPI_INTEGRITY_SECRET', 'test_secret_dummy')
    
    cadena_a_firmar = f"{referencia_unica}{monto_centavos}{moneda}{secreto_integridad}"
    firma_sha256 = hashlib.sha256(cadena_a_firmar.encode('utf-8')).hexdigest()

    headers = {
        "Authorization": f"Bearer {settings.WOMPI_PRIVATE_KEY}",
        "Content-Type": "application/json"
    }

    try:
        merchant_res = requests.get(f"https://production.wompi.co/v1/merchants/{settings.WOMPI_PUBLIC_KEY}")
        merchant_data = merchant_res.json()
        acceptance_token = merchant_data.get('data', {}).get('presigned_acceptance', {}).get('acceptance_token')

        if not acceptance_token:
            return Response({"error": "No se pudo obtener el token de aceptación de Wompi."}, status=status.HTTP_400_BAD_REQUEST)

        url_transaccion = "https://production.wompi.co/v1/transactions"
        payload = {
            "amount_in_cents": monto_centavos,
            "currency": moneda,
            "customer_email": email_cliente,
            "payment_method": {
                "type": "CARD",
                "token": token_tarjeta,
                "installments": 1
            },
            "reference": referencia_unica,
            "acceptance_token": acceptance_token,
            "signature": firma_sha256
        }

        response = requests.post(url_transaccion, json=payload, headers=headers)
        data_wompi = response.json()

        estado_transaccion = data_wompi.get('data', {}).get('status')
        
        if response.status_code == 201 and (estado_transaccion == 'APPROVED' or estado_transaccion == 'PENDING'):
            transaccion_id = data_wompi['data']['id']

            # --- NUEVO: Guardar el registro en la Base de Datos de Django ---
            try:
                TransaccionPago.objects.create(
                    nombre_cliente=nombre_cliente,
                    email_cliente=email_cliente,
                    telefono_cliente=telefono_cliente,
                    producto_id=producto_id,
                    producto_titulo=producto_titulo,
                    monto=precio,
                    transaccion_id_wompi=transaccion_id,
                    referencia_wompi=referencia_unica,
                    estado=estado_transaccion
                )
            except Exception as db_error:
                print(f"Error al guardar transacción en BD: {db_error}")


            # 1. CORREO DE ALERTA PARA TI (info@gegova.com.co)
            try:
                asunto_admin = f"🚨 ¡NUEVA VENTA! - {producto_titulo}"
                mensaje_admin = (
                    f"Se ha procesado un nuevo pago exitoso en GEGOVA:\n\n"
                    f"👤 DATOS DEL CLIENTE:\n"
                    f"• Nombre: {nombre_cliente}\n"
                    f"• Correo: {email_cliente}\n"
                    f"• Teléfono / WhatsApp: {telefono_cliente}\n\n"
                    f"📦 DETALLES DEL PEDIDO:\n"
                    f"• Producto: {producto_titulo} (ID: {producto_id})\n"
                    f"• Valor Pagado: ${precio} COP\n"
                    f"• Referencia Wompi: {data_wompi['data']['id']}\n\n"
                    f"⚠️ ACCIÓN REQUERIDA:\n"
                    f"Por favor adquiere la licencia/producto y envíasela al cliente a su correo ({email_cliente})."
                )
                send_mail(
                    asunto_admin,
                    mensaje_admin,
                    settings.DEFAULT_FROM_EMAIL,
                    ['dirsistemas@gegova.com.co'],
                    fail_silently=False,
                )
            except Exception as e:
                print(f"Error al enviar notificación a admin: {e}")

            # 2. CORREO AUTOMÁTICO DE CONFIRMACIÓN PARA EL CLIENTE
            # 2. CORREO HTML ELEGANTE PARA EL CLIENTE
            try:
                asunto_cliente = f"¡Pago recibido con éxito! - {producto_titulo} | GEGOVA"
                
                # Contexto para alimentar la plantilla HTML
                contexto_email = {
                    'nombre_cliente': nombre_cliente,
                    'producto_titulo': producto_titulo,
                    'precio': f"{int(precio):,}".replace(",", "."), # Formatea precio ej: 85.000
                    'transaccion_id': transaccion_id,
                }
                
                # Renderizar la plantilla HTML
                html_message = render_to_string('emails/confirmacion_pago.html', contexto_email)
                plain_message = f"Hola {nombre_cliente}, hemos confirmado tu pago por {producto_titulo}. En unos momentos recibirás tu producto."

                send_mail(
                    subject=asunto_cliente,
                    message=plain_message, # Versión texto plano de respaldo
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    recipient_list=[email_cliente],
                    html_message=html_message, # <-- AQUÍ SE ENVÍA EL HTML
                    fail_silently=False
                )
            except Exception as e:
                print(f"Error correo HTML cliente: {e}")

            return Response({"mensaje": "¡Pago procesado exitosamente!", "transaccion": transaccion_id}, status=status.HTTP_200_OK)
        else:
            error_msg = data_wompi.get('error', {}).get('messages', 'Pago declinado.')
            print(f"Error detallado de Wompi en backend: {data_wompi}")
            return Response({"error": error_msg}, status=status.HTTP_400_BAD_REQUEST)

    except Exception as e:
        print(f"Excepción interna en Django: {e}")
        return Response({"error": "Error interno al procesar el pago."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



@api_view(['POST'])
@permission_classes([AllowAny])
def webhook_wompi(request):
    """
    Endpoint al que Wompi notifica de forma asíncrona (Servidor a Servidor)
    cuando una transacción cambia de estado (APPROVED, DECLINED, PENDING, etc.)
    """
    payload = request.data
    event = payload.get('event')

    # Solo procesamos eventos de actualización de transacción
    if event == 'transaction.updated':
        data_tx = payload.get('data', {}).get('transaction', {})
        
        tx_id = data_tx.get('id')
        referencia = data_tx.get('reference')
        estado = data_tx.get('status')  # APPROVED, DECLINED, VOIDED, PENDING
        monto_centavos = data_tx.get('amount_in_cents', 0)
        precio_cop = int(monto_centavos / 100)
        
        email_cliente = data_tx.get('customer_email')
        
        # Extraemos nombre y teléfono si vienen en los metadatos o customer_data
        customer_data = data_tx.get('customer_data') or {}
        nombre_cliente = customer_data.get('full_name', 'Cliente GEGOVA')
        telefono_cliente = customer_data.get('phone_number', 'No especificado')

        # Extraemos el ID/Título del producto de la referencia (ej: GEGOVA_lic-indiv_1792...)
        partes_ref = referencia.split('_') if referencia else []
        producto_id = partes_ref[1] if len(partes_ref) > 1 else 'Producto GEGOVA'

        # --- OPCIONAL: Validación de firma checksum enviada por Wompi ---
        # event_secret = getattr(settings, 'WOMPI_EVENTS_SECRET', '')
        # timestamp = payload.get('timestamp')
        # checksum = payload.get('signature', {}).get('checksum')
        # ---------------------------------------------------------------

        # 1. Crear o actualizar la transacción en la Base de Datos
        transaccion_obj, created = TransaccionPago.objects.get_or_create(
            referencia_wompi=referencia,
            defaults={
                'transaccion_id_wompi': tx_id,
                'nombre_cliente': nombre_cliente,
                'email_cliente': email_cliente,
                'telefono_cliente': telefono_cliente,
                'producto_id': producto_id,
                'producto_titulo': producto_id,
                'monto': precio_cop,
                'estado': estado
            }
        )

        # Si ya existía, actualizamos el estado
        estado_anterior = transaccion_obj.estado
        transaccion_obj.estado = estado
        transaccion_obj.transaccion_id_wompi = tx_id
        transaccion_obj.save()

        # 2. Si el pago fue APROBADO y antes no estaba marcado como tal, enviamos las notificaciones
        if estado == 'APPROVED' and estado_anterior != 'APPROVED':
            
            # Notificación de alerta para el Administrador
            try:
                asunto_admin = f"🚨 ¡PAGO CONFIRMADO VIA WEBHOOK! - {producto_id}"
                mensaje_admin = (
                    f"Wompi ha confirmado la aprobación del pago vía Webhook:\n\n"
                    f"👤 CLIENTE:\n"
                    f"• Correo: {email_cliente}\n"
                    f"• Nombre: {nombre_cliente}\n\n"
                    f"📦 PEDIDO:\n"
                    f"• Referencia: {referencia}\n"
                    f"• ID Wompi: {tx_id}\n"
                    f"• Monto: ${precio_cop:,} COP\n\n"
                    f"⚠️ Por favor proceda con la entrega de la licencia/servicio."
                )
                send_mail(asunto_admin, mensaje_admin, settings.DEFAULT_FROM_EMAIL, ['dirsistemas@gegova.com.co'], fail_silently=True)
            except Exception as e:
                print(f"Error al enviar notificación Webhook admin: {e}")

            # Correo HTML de confirmación para el Cliente
            try:
                contexto_email = {
                    'nombre_cliente': nombre_cliente,
                    'producto_titulo': producto_id,
                    'precio': f"{precio_cop:,}".replace(",", "."),
                    'transaccion_id': tx_id,
                }
                html_message = render_to_string('emails/confirmacion_pago.html', contexto_email)
                plain_message = f"Hola, hemos confirmado tu pago por {producto_id}. En unos momentos recibirás tu producto."

                send_mail(
                    subject=f"¡Pago recibido con éxito! - {producto_id} | GEGOVA",
                    message=plain_message,
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    recipient_list=[email_cliente],
                    html_message=html_message,
                    fail_silently=True
                )
            except Exception as e:
                print(f"Error al enviar correo Webhook cliente: {e}")

    # Respondemos 200 OK a Wompi para confirmar recepción
    return Response({"status": "received"}, status=status.HTTP_200_OK)