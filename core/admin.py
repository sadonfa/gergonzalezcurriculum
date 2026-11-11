from django.contrib import admin
from .models import Category, Post, Curriculum

# Register your models here.

class AdminCategory(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('name',  'created' )

class AdminPost(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('title', 'author', 'published')

@admin.register(Curriculum)
class CurriculumAdmin(admin.ModelAdmin):
    list_display = ('title', 'archivo', 'fecha_actualizacion')

admin.site.register(Category, AdminCategory)
admin.site.register(Post, AdminPost)