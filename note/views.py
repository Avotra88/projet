
from django.shortcuts import render, redirect
from .models import Etudiant
from .forms import EtudiantForm
from django.shortcuts import render
from django.http import HttpResponse
import weasyprint
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



def generer_pdp(request, etudiant_id):
    etudiant = Etudiant.objects.get(id=etudiant_id)
    photo_url = etudiant.photo.url  # URL de la photo de l'étudiant (assurez-vous que le champ photo existe)

    # Créer le contexte pour le template
    context = {
        'etudiant': etudiant,
        'photo_url': photo_url
    }

    # Rendre le HTML à partir du template
    html = render(request, 'carte_etudiant.html', context)

    # Convertir le HTML en PDF avec WeasyPrint
    pdf_file = weasyprint.HTML(string=html.content.decode('utf-8')).write_pdf()

    # Retourner le PDF dans la réponse
    response = HttpResponse(pdf_file, content_type='application/pdf')
    response['Content-Disposition'] = f'inline; filename="carte_etudiant_{etudiant.matricule}.pdf"'
    return response

# from reportlab.lib.pagesizes import letter
# from reportlab.pdfgen import canvas

# def generer_pdp(request, etudiant_id):
#     etudiant = Etudiant.objects.get(id=etudiant_id)
#     response = HttpResponse(content_type='application/pdf')
#     response['Content-Disposition'] = f'inline; filename="carte_etudiant_{etudiant.matricule}.pdf"'
    
#     # Créez un objet PDF
#     p = canvas.Canvas(response, pagesize=letter)

#     # Ajoutez le contenu à la page PDF
#     p.drawString(100, 750, f"Nom: {etudiant.nom}")
#     p.drawString(100, 730, f"Prénom: {etudiant.prenom}")
#     p.drawString(100, 710, f"Matricule: {etudiant.matricule}")
#     p.drawString(100, 690, f"Programme: {etudiant.programme}")

#     # Ajoutez une image de la photo de l'étudiant (si disponible)
#     photo_url = etudiant.photo.url
#     if photo_url:
#         p.drawImage(photo_url, 400, 700, width=100, height=100)

#     p.showPage()
#     p.save()

#     return response
