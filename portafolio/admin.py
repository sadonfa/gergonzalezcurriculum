from django.contrib import admin
from .models import Category, Portfolio

# Register your models here.

class AdminCategory(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('title',  'created' )

class AdminPortfolio(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('title', 'created')

admin.site.register(Category, AdminCategory)
admin.site.register(Portfolio, AdminPortfolio)