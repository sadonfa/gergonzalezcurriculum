from django.db import models
from django_ckeditor_5.fields import CKEditor5Field

# Create your models here.

class Certificate(models.Model):
    title = models.CharField(max_length=150, verbose_name="Titulo")
    verificate = models.CharField(max_length=150, verbose_name="Id de verificacion")
    data_certi = models.DateField(verbose_name="Fecha de certificado")
    logo = models.ImageField(upload_to="certificate", verbose_name="Logo")
    created = models.DateField(auto_now_add=True, verbose_name='Creacion' )
    updated = models.DateField(auto_now=True, verbose_name='Actualizacion' )

    class Meta:
        verbose_name = "Certificado"
        verbose_name_plural = "Certificados"

    def __str__(self):
        return self.title
    

class Knowledges(models.Model):
    title = models.CharField(max_length=150, verbose_name="Titulo")
    created = models.DateField(auto_now_add=True, verbose_name='Creacion' )
    updated = models.DateField(auto_now=True, verbose_name='Actualizacion' )

    class Meta:
        verbose_name = "Conocimiento"
        verbose_name_plural = "Conocimientos"

    def __str__(self):
        return self.title
    
class SkillsCode(models.Model):
    title = models.CharField(max_length=150, verbose_name="Titulo")
    percentage = models.IntegerField(verbose_name="Porcentaje")
    created = models.DateField(auto_now_add=True, verbose_name='Creacion' )
    updated = models.DateField(auto_now=True, verbose_name='Actualizacion' )

    class Meta:
        verbose_name = "Habilidades de Codigo"
        verbose_name_plural = "Habilidades de Codigos"

    def __str__(self):
        return self.title
    
class SkillsDesing(models.Model):
    title = models.CharField(max_length=150, verbose_name="Titulo")
    percentage = models.IntegerField(verbose_name="Porcentaje")
    created = models.DateField(auto_now_add=True, verbose_name='Creacion' )
    updated = models.DateField(auto_now=True, verbose_name='Actualizacion' )

    class Meta:
        verbose_name = "Habilidades de Diseño"
        verbose_name_plural = "Habilidades de Diseños"

    def __str__(self):
        return self.title
    

class Training(models.Model):
    title = models.CharField(max_length=100, verbose_name="Titulo")
    description =  models.TextField(verbose_name='Descripcion')
    year = models.IntegerField(verbose_name="Año")
    company = models.CharField(max_length=150, verbose_name="Compañia")
    created = models.DateField(auto_now_add=True, verbose_name='Creacion' )
    updated = models.DateField(auto_now=True, verbose_name='Actualizacion' )

    class Meta:
        verbose_name = "Formacion"
        verbose_name_plural = "Formaciones"
        ordering = ['year']

    def __str__(self):
        return self.title
    
class Experience(models.Model):
    title = models.CharField(max_length=100, verbose_name="Titulo")
    description =  models.TextField(verbose_name='Descripcion')
    year = models.CharField(max_length=100, verbose_name="Año")
    company = models.CharField(max_length=150, verbose_name="Compañia")
    created = models.DateField(auto_now_add=True, verbose_name='Creacion' )
    updated = models.DateField(auto_now=True, verbose_name='Actualizacion' )

    class Meta:
        verbose_name = "Experiencia"
        verbose_name_plural = "Experiencias"

    def __str__(self):
        return self.title