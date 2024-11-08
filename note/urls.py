from django.urls import path, include
from . import views
from django.contrib import admin
from note import views


urlpatterns = [
    path('gestion_etudiants/', views.gestion_etudiants, name='gestion_etudiants'),
    
]