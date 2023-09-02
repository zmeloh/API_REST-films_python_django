from django.db import models
from django.contrib.auth.models import User

class Film(models.Model):
    titre = models.CharField(max_length=100)
    description = models.TextField()
    annee_sortie = models.PositiveIntegerField()
    # Ajoutez d'autres champs selon vos besoins

    def __str__(self):
        return self.titre

class Favorite(models.Model):
    utilisateur = models.ForeignKey(User, on_delete=models.CASCADE)
    film = models.ForeignKey(Film, on_delete=models.CASCADE)
    # Ajoutez d'autres champs selon vos besoins

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    # Ajoutez d'autres champs pour les informations de l'utilisateur

# Si vous souhaitez ajouter d'autres modèles, vous pouvez les ajouter ici.
