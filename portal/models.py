from django.db import models

class SolicitudContacto(models.Model):
    nombre = models.CharField(max_length=150)
    email = models.EmailField()
    servicio = models.CharField(max_length=100)
    mensaje = models.TextField(blank=True, null=True)
    creado_en = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Solicitud de Contacto"
        verbose_name_plural = "Solicitudes de Contacto"
        ordering = ['-creado_en']

    def __str__(self):
        return f"{self.nombre} - {self.servicio}"