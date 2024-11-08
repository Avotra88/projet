from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('note.urls')),  # Incluez les URLs de l'application
]
