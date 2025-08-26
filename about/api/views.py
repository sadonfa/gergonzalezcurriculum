from ..serializers import AboutSerializer, ClientSerializer
from about.models import Skills, Client
from rest_framework import viewsets


class SkillsViewSet(viewsets.ModelViewSet):
  queryset = Skills.objects.all()
  serializer_class = AboutSerializer


class ClientViewSet(viewsets.ModelViewSet):
  queryset = Client.objects.all()
  serializer_class = ClientSerializer