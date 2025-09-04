from django.urls import path
from .views import Certificates, Knowlenges, SkillsCodes, SkillsDesings, Experiences, Trainings

urlpatterns = [
    path('curriculum/certificates/', Certificates.as_view()),
    path('curriculum/knowlenges/', Knowlenges.as_view()),
    path('curriculum/skillscodes/', SkillsCodes.as_view()),
    path('curriculum/skillsdesings/', SkillsDesings.as_view()),
    path('curriculum/experiences/', Experiences.as_view()),
    path('curriculum/trainings/', Trainings.as_view()),
]
