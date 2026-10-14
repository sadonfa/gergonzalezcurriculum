from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from django.core.mail import send_mail
from django.conf import settings
from .serializers import SolicitudContactoSerializer

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