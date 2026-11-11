from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Post, Category, Curriculum
from .serializers import PostSerializer, CategorySerializer, CurriculumSerializer
from rest_framework import viewsets

# Create your views here.

def home(request):

  return render(request, 'home.html', {
    'title': 'Repositorios de GEGOVA',
  })

class CategoriesViewSet(viewsets.ModelViewSet):
  queryset = Category.objects.all()
  serializer_class = CategorySerializer


class PostViewSet(viewsets.ModelViewSet):
  queryset = Post.objects.all()
  serializer_class = PostSerializer


@api_view(['GET'])
def obtener_ultimo_cv(request):
    cv = Curriculum.objects.last()
    if cv:
        serializer = CurriculumSerializer(cv, context={'request': request})
        return Response(serializer.data)
    return Response({'error': 'No hay CV disponible'}, status=status.HTTP_404_NOT_FOUND)