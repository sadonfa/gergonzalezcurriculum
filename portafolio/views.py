from django.shortcuts import render
from .models import Portfolio as ModPortafolio

from .serializers import PortafolioSerializer
from rest_framework.views import APIView
from django.http.response import JsonResponse, Http404
from http import HTTPStatus

# Create your views here.

class Portafolio(APIView):

    def get(self, request):
        data = ModPortafolio.objects.order_by('-id').all()
        data_json = PortafolioSerializer(data, many=True)

        return JsonResponse({"data": data_json.data}, status=HTTPStatus.OK)