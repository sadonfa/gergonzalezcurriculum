from django.shortcuts import render
from .models import Post as ModPost

from .serializers import PostSerializer
from rest_framework.views import APIView
from django.http.response import JsonResponse, Http404
from http import HTTPStatus

# Create your views here.

class Post(APIView):

    def get(self, request):
        data = ModPost.objects.order_by('-id').all()
        data_json = PostSerializer(data, many=True)

        return JsonResponse({"data": data_json.data}, status=HTTPStatus.OK)