from django.db import models
from django_ckeditor_5.fields import CKEditor5Field

# Create your models here.

class Skills(models.Model):
    title = models.CharField(max_length=150, verbose_name="Titulo")
    icon =  models.CharField(max_length=200, verbose_name="ICON")
    #description = CKEditor5Field('Text', config_name='extends')
    description = models.TextField(verbose_name='Descripcion')
    created = models.DateField(auto_now_add=True, verbose_name='Creacion' )
    updated = models.DateField(auto_now=True, verbose_name='Actualizacion' )

    class Meta:
        verbose_name = "Habilidad"
        verbose_name_plural = "Habilidades"

    def __str__(self):
        return self.title
    

class Client(models.Model):
    title = models.CharField(max_length=150, verbose_name="Titulo")
    image = models.ImageField(upload_to="Clients", verbose_name="Imagen")
    link = models.URLField( default="null",  verbose_name="LINK")
    created = models.DateField(auto_now_add=True, verbose_name='Creacion' )
    updated = models.DateField(auto_now=True, verbose_name='Actualizacion' )

    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"

    def __str__(self):
        return self.title
    

class Review(models.Model):
    name = models.CharField(max_length=150, verbose_name="Nombre")
    subject = models.CharField(max_length=150, verbose_name="Titulo")
    email = models.CharField(max_length=150, verbose_name="Correo")
    photo = models.ImageField(default="imagen.png", upload_to="Reviews", verbose_name="Foto" )
    messege = models.TextField(verbose_name="Mensaje")
    created = models.DateField(auto_now_add=True, verbose_name='Creacion' )
    updated = models.DateField(auto_now=True, verbose_name='Actualizacion' )

    class Meta:
        verbose_name = "Reseña"
        verbose_name_plural = "Reseñas"

    def __str__(self):
        return self.name
    
    