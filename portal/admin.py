from django.contrib import admin
from .models import SolicitudContacto

@admin.register(SolicitudContacto)
class SolicitudContactoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'email', 'servicio', 'creado_en')
    list_filter = ('servicio', 'creado_en')
    # search_fields = ('nombre', 'email', 'mensaje')
    readonly_fields = ('creado_en',)