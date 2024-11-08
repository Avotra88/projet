
from django.shortcuts import render, redirect
from .models import Etudiant
from .forms import EtudiantForm
from django.shortcuts import render
from django.http import HttpResponse
from .models import Etudiant  # Assurez-vous d'avoir ce modèle configuré



def gestion_etudiants(request):
    if request.method == 'POST':
        form = EtudiantForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('gestion_etudiants')
    else:
        form = EtudiantForm()

    etudiants = Etudiant.objects.all()
    return render(request, 'gestion_etudiants.html', {'form': form, 'etudiants': etudiants})


