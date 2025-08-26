from django.shortcuts import render
from .models import Certificate as ModCertificate, Knowledges as ModKnowledges, SkillsCode as ModSkillsCode, SkillsDesing as ModSkillsDesing, Training as ModTrainings, Experience as ModExperience
from .serializers import CertificateSerializer, KnowledgesSerializer, SkillsCodeSerializer, SkillsDesingsSerializer, ExperienceSerializer, TrainingSerializer
from rest_framework.views import APIView
from django.http.response import JsonResponse, Http404
from http import HTTPStatus
# Create your views here.

class Certificates(APIView):

    def get(self, request):
        data = ModCertificate.objects.order_by('-id').all()
        data_json = CertificateSerializer(data, many=True)

        # return JsonResponse(data_json.data, safe=False)
        return JsonResponse({"data": data_json.data}, status=HTTPStatus.OK)
    
    # def post(self, request):
        
    #     try:
    #         mCategoria.objects.create(name=request.data['nombre'])
    #         return JsonResponse({'estado': 'ok', 'mensaje':'producto creado con exito.'}, status=HTTPStatus.CREATED)
    #     except Exception as e:
    #         raise Http404

class Knowlenges(APIView):

    def get(self, request):
        data = ModKnowledges.objects.order_by('-id').all()
        data_json = KnowledgesSerializer(data, many=True)

        # return JsonResponse(data_json.data, safe=False)
        return JsonResponse({"data": data_json.data}, status=HTTPStatus.OK)
    

class SkillsCodes(APIView):

    def get(self, request):
        data = ModSkillsCode.objects.order_by('-id').all()
        data_json = SkillsCodeSerializer(data, many=True)

        return JsonResponse({"data": data_json.data}, status=HTTPStatus.OK)

class SkillsDesings(APIView):

    def get(self, request):
        data = ModSkillsDesing.objects.order_by('-id').all()
        data_json = SkillsDesingsSerializer(data, many=True)

        return JsonResponse({"data": data_json.data}, status=HTTPStatus.OK)
    

class Experiences(APIView):

    def get(self, request):
        data = ModExperience.objects.order_by('-id').all()
        data_json = ExperienceSerializer(data, many=True)

        return JsonResponse({"data": data_json.data}, status=HTTPStatus.OK)
    

class Trainings(APIView):

    def get(self, request):
        data = ModTrainings.objects.order_by('-id').all()
        data_json = TrainingSerializer(data, many=True)

        return JsonResponse({"data": data_json.data}, status=HTTPStatus.OK)