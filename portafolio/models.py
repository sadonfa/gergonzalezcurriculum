from django.db import models
from django_ckeditor_5.fields import CKEditor5Field

# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=200, verbose_name="Nombre")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Creado el")
    updated = models.DateTimeField(auto_now=True, verbose_name="Editado el")

    class Meta:
        verbose_name="Categoria"
        verbose_name_plural="Categorias"
        ordering=['-created']

    def __str__(self):
        return f'{self.title}' 
    

class Portfolio(models.Model):
    title = models.CharField(max_length=200, verbose_name="Nombre")
    icon = models.CharField(max_length=100, verbose_name="icono")
    category = models.ForeignKey(Category, verbose_name="Categoria", on_delete=models.CASCADE)
    image =  models.ImageField(default="null", upload_to="tours")
    url = models.URLField(default="null", verbose_name="URL")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Creado el")
    updated = models.DateTimeField(auto_now=True, verbose_name="Editado el")

    class Meta:
        verbose_name="Portafolio"
        verbose_name_plural="Portafolio"

    def __str__(self):
        return f'{self.title}' 