from django.contrib import admin
from .models import SolicitudContacto, TransaccionPago

@admin.register(SolicitudContacto)
class SolicitudContactoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'email', 'servicio', 'creado_en')
    list_filter = ('servicio', 'creado_en')
    # search_fields = ('nombre', 'email', 'mensaje')
    readonly_fields = ('creado_en',)


@admin.register(TransaccionPago)
class TransaccionPagoAdmin(admin.ModelAdmin):
    list_display = ('transaccion_id_wompi', 'nombre_cliente', 'email_cliente', 'producto_titulo', 'monto', 'estado', 'creado_en')
    list_filter = ('estado', 'creado_en')
    search_fields = ('nombre_cliente', 'email_cliente', 'transaccion_id_wompi', 'referencia_wompi')
    readonly_fields = ('creado_en',)