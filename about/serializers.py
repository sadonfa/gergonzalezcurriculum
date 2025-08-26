from .models import Skills, Client, Review
from rest_framework import serializers


class ClientSerializer(serializers.ModelSerializer):

  class Meta:
      model = Client
      fields = ['id', 'title', 'image', 'link', 'created']

class SkillsSerializer(serializers.ModelSerializer):

   class Meta:
       model = Skills
       fields = '__all__'

class ReviewSerializer(serializers.ModelSerializer):

  class Meta:
      model = Review
      fields = '__all__'