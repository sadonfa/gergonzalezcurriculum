from .models import Post, Category
from django.contrib.auth.models import User
from rest_framework import serializers

class CategorySerializer(serializers.ModelSerializer):

  class Meta:
    model = Category
    fields = ['id', 'name']
    # fields = '__all__'  

class AuthorSerializer(serializers.ModelSerializer):

  class Meta:
    model = User
    fields = ['id', 'username', 'last_name', 'first_name', 'email' ]
    # fields = '__all__'  

class PostSerializer(serializers.ModelSerializer):

  category_name = CategorySerializer(source='categories', read_only=True)
  author_db = AuthorSerializer(source='author', read_only=True)

  # category_name = serializers(source="categories.name", read_only=True)

  class Meta:
      model = Post
      fields = ['id', 'title', 'description', 'category_name', 'author_db']
      # fields = '__all__'