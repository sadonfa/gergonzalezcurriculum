from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('home/', views.home),
    path('api/obtener-cv/', views.obtener_ultimo_cv, name='obtener_cv'),
]
