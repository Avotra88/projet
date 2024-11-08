from django.db import models

class Etudiant(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    date_naissance = models.DateField()
    photo = models.ImageField(upload_to='photos_etudiants/', null=True, blank=True)
    note_maths = models.FloatField()
    note_physique = models.FloatField()
    note_informatique = models.FloatField()
    note_moyenne = models.FloatField(null=True, blank=True)

    def save(self, *args, **kwargs):
        self.note_moyenne = (self.note_maths + self.note_physique + self.note_informatique) / 3
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.prenom} {self.nom}"
