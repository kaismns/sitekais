from django.urls import path
from .views import projects, acceuil, CV, contact

app_name = 'core'


urlpatterns= [
    path('', acceuil, name='acceuil'),
    path('CV/', CV, name='CV'),
    path('projects/', projects, name='projects'),
    path('contact/', contact, name='contact'),
]
