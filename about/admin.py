from django.contrib import admin
from .models import Skills, Client, Review

# Register your models here.

class AdminSkills(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('title',  'created')

class AdminClient(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('title',  'created')

class AdminReview(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('name',  'created')

admin.site.register(Skills, AdminSkills)
admin.site.register(Client, AdminClient)
admin.site.register(Review, AdminReview)