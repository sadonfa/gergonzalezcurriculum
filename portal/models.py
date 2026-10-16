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

class TransaccionPago(models.Model):
    ESTADOS = (
        ('APPROVED', 'Aprobado'),
        ('PENDING', 'Pendiente'),
        ('DECLINED', 'Declinado'),
        ('ERROR', 'Error'),
    )

    nombre_cliente = models.CharField(max_length=150)
    email_cliente = models.EmailField()
    telefono_cliente = models.CharField(max_length=50, blank=True, null=True)
    
    producto_id = models.CharField(max_length=100)
    producto_titulo = models.CharField(max_length=200)
    monto = models.DecimalField(max_digits=12, decimal_places=2)
    
    transaccion_id_wompi = models.CharField(max_length=100, unique=True)
    referencia_wompi = models.CharField(max_length=100, unique=True)
    estado = models.CharField(max_length=20, choices=ESTADOS, default='PENDING')
    
    creado_en = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Transacción de Pago"
        verbose_name_plural = "Transacciones de Pago"
        ordering = ['-creado_en']

    def __str__(self):
        return f"{self.producto_titulo} - {self.nombre_cliente} (${self.monto} COP)"