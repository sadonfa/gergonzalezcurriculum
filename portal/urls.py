from django.urls import path
from .views import registrar_contacto, procesar_pago_wompi, webhook_wompi

urlpatterns = [
    path('contacto/', registrar_contacto, name='portal-contacto'),
    path('pagos/wompi/', procesar_pago_wompi, name='procesar_pago_wompi'),
    path('pagos/webhook/', webhook_wompi, name='webhook_wompi'),
]