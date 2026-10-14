from rest_framework import serializers
from .models import SolicitudContacto

class SolicitudContactoSerializer(serializers.ModelSerializer):
    class Meta:
        model = SolicitudContacto
        fields = ['id', 'nombre', 'email', 'servicio', 'mensaje', 'creado_en']