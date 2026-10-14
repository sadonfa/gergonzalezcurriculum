from django.urls import path
from .views import registrar_contacto

urlpatterns = [
    path('contacto/', registrar_contacto, name='portal-contacto'),
]