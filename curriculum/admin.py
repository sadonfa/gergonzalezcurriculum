from django.contrib import admin
from .models import Certificate, Knowledges, SkillsCode, SkillsDesing, Experience, Training

# Register your models here.

class AdminCertificate(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('title',  'created')

class AdminKnowledges(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('title',  'created')

class AdminSkillsCode(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('title',  'percentage')

class AdminSkillDesing(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('title',  'percentage')

class AdminTraining(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('title',  'year', 'company' )

class AdminExperience(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('title',  'year', 'company')

admin.site.register(Certificate, AdminCertificate)
admin.site.register(Knowledges, AdminKnowledges)
admin.site.register(SkillsCode, AdminSkillsCode)
admin.site.register(SkillsDesing, AdminSkillDesing)
admin.site.register(Training, AdminTraining)
admin.site.register(Experience, AdminExperience)