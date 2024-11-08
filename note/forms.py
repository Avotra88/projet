from django import forms
from .models import Etudiant

class EtudiantForm(forms.ModelForm):
    class Meta:
        model = Etudiant
        fields = ['nom', 'prenom', 'date_naissance', 'photo', 'note_maths', 'note_physique', 'note_informatique']
