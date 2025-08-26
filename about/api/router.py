from django.urls import path
from rest_framework import routers
from .views import SkillsViewSet, ClientViewSet

router_skills = routers.DefaultRouter()

router_skills.register(
    prefix='skills', basename='skills', viewset=SkillsViewSet,
    # prefix='about/client/', basename='client', viewset=ClientViewSet,
)
    
# urlpatterns = [
#     path('about/client/', ClientViewSet, name='client'),
#     # path('auth/me/', UserView.as_views())
# ]


# router_about.register('post', AboutViewSet)   