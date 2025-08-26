from django.urls import path
from .views import Client, Skills, Reviews

urlpatterns = [
    path('about/clients/', Client.as_view()),
    path('about/skills/', Skills.as_view()),
    path('about/reviews/', Reviews.as_view()),
]
