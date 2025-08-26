from django.db import models
from django.utils import timezone       
from django.contrib.auth.models import User

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nombre")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Creado el")
    updated = models.DateTimeField(auto_now=True, verbose_name="Actualizado el")

    class Meta:
        verbose_name="Categoria"
        verbose_name_plural="Categorias"
        ordering = ['-created']

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=150, verbose_name="Titulo")
    description = models.TextField(verbose_name="description")
    image = models.ImageField(default="null", upload_to="blog")
    categories = models.ForeignKey(Category, verbose_name="Categorias", on_delete=models.CASCADE)
    author = models.ForeignKey(User, verbose_name="Autor" , on_delete=models.CASCADE)
    published = models.BooleanField(default=False, verbose_name="Publicado")
    published_date = models.DateTimeField(verbose_name="Fecha de publicacion", default=timezone.now)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Creado el")
    updated = models.DateTimeField(auto_now=True, verbose_name="Actualizado el")

    class Meta:
        verbose_name="Entrada"
        verbose_name_plural="Entradas"
        ordering = ['-published']
    def __str__(self):
        return self.title