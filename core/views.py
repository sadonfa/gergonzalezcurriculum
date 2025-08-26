from django.shortcuts import render
from .models import Post, Category
from .serializers import PostSerializer, CategorySerializer
from rest_framework import viewsets

# Create your views here.

class CategoriesViewSet(viewsets.ModelViewSet):
  queryset = Category.objects.all()
  serializer_class = CategorySerializer


class PostViewSet(viewsets.ModelViewSet):
  queryset = Post.objects.all()
  serializer_class = PostSerializer