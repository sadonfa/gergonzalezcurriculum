from django.shortcuts import render
from .models import Skills as ModSkills, Client as ModClient, Review as ModReview

from .serializers import  ClientSerializer, SkillsSerializer, ReviewSerializer

from rest_framework.views import APIView
from django.http.response import JsonResponse, Http404
from http import HTTPStatus

# Create your views here.


class Client(APIView):

    def get(self, request):
        data = ModClient.objects.order_by('-id').all()
        data_json = ClientSerializer(data, many=True)

        # return JsonResponse(data_json.data, safe=False)
        return JsonResponse({"data": data_json.data}, status=HTTPStatus.OK)
    
    # def post(self, request):
        
    #     try:
    #         mCategoria.objects.create(name=request.data['nombre'])
    #         return JsonResponse({'estado': 'ok', 'mensaje':'producto creado con exito.'}, status=HTTPStatus.CREATED)
    #     except Exception as e:
    #         raise Http404
    

class Skills(APIView):

    def get(self, request):
        data = ModSkills.objects.order_by('-id').all()
        data_json = SkillsSerializer(data, many=True)

        # return JsonResponse(data_json.data, safe=False)
        return JsonResponse({"data": data_json.data}, status=HTTPStatus.OK)
    
    # def post(self, request):
        
    #     try:
    #         mCategoria.objects.create(name=request.data['nombre'])
    #         return JsonResponse({'estado': 'ok', 'mensaje':'producto creado con exito.'}, status=HTTPStatus.CREATED)
    #     except Exception as e:
    #         raise Http404
    

class Reviews(APIView):

    def get(self, request):
        data = ModReview.objects.order_by('-id').all()
        data_json = ReviewSerializer(data, many=True)

        # return JsonResponse(data_json.data, safe=False)
        return JsonResponse({"data": data_json.data}, status=HTTPStatus.OK)
    
    # def post(self, request):
        
    #     try:
    #         mCategoria.objects.create(name=request.data['nombre'])
    #         return JsonResponse({'estado': 'ok', 'mensaje':'producto creado con exito.'}, status=HTTPStatus.CREATED)
    #     except Exception as e:
    #         raise Http404
    