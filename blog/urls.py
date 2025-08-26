from django.urls import path
from .views import Post

urlpatterns = [
    path('blog/posts/', Post.as_view()),
]
