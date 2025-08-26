from .models import Portfolio
from rest_framework import serializers


class PortafolioSerializer(serializers.ModelSerializer):

  class Meta:
      model = Portfolio
      fields = "__all__"