from django.urls import path, include
from . import views
from django.contrib import admin
from note import views


urlpatterns = [
    path('gestion_etudiants/', views.gestion_etudiants, name='gestion_etudiants'),
    path('carte_etudiant/<int:etudiant_id>/', views.generer_pdp, name='carte_etudiant'),
]