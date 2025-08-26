from .models import Certificate, Knowledges, SkillsCode, SkillsDesing, Experience, Training
from rest_framework import serializers


class CertificateSerializer(serializers.ModelSerializer):

  class Meta:
      model = Certificate
      fields = "__all__"

class KnowledgesSerializer(serializers.ModelSerializer):

  class Meta:
      model = Knowledges
      fields = "__all__"

class SkillsCodeSerializer(serializers.ModelSerializer):

  class Meta:
      model = SkillsCode
      fields = "__all__"

class SkillsDesingsSerializer(serializers.ModelSerializer):

  class Meta:
      model = SkillsDesing
      fields = "__all__"

class ExperienceSerializer(serializers.ModelSerializer):

  class Meta:
      model = Experience
      fields = "__all__"

class TrainingSerializer(serializers.ModelSerializer):

  class Meta:
      model = Training
      fields = "__all__"