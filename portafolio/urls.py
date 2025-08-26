from django.urls import path
from .views import Portafolio

urlpatterns = [
    path('portafolio/', Portafolio.as_view()),
]
