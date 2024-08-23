from django.db import models
#from django.contrib.auth.models import User

class Perfil(models.Model):
    cliente = models.CharField(max_length=100, null=True, blank=True) #User.username
    bio = models.TextField(null=True, blank=True)
    foto = models.ImageField(upload_to="fotos_perfil/", null=True, blank=True)
