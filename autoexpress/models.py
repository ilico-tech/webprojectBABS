from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Voiture(models.Model):
    STATUS=(('Disponible','Disponible'),
           ('Indispobible','Indisponible'))
    SERVICE = (('Location', 'Location'),
               ('Livraision', 'Livraision'),
               ('Course','Course'))


    image=models.ImageField(upload_to="",null=True,blank=True)
    image1 = models.ImageField(upload_to="", null=True, blank=True)
    image2 = models.ImageField(upload_to="", null=True, blank=True)
    status=models.CharField(max_length=20,null=True,blank=True,choices=STATUS,default='Disponible')
    service=models.CharField(max_length=20,null=True,blank=True,choices=SERVICE,default='Course')
    marque=models.CharField(max_length=20,null=True,blank=True)
    categorie=models.CharField(max_length=50,null=True,blank=True)
    emplacement=models.CharField(max_length=50,null=True,blank=True)
    annee = models.IntegerField(null=True, blank=True)
    carburant = models.CharField(max_length=10, null=True, blank=True)
    kilometrage = models.PositiveIntegerField(null=True, blank=True)
    boitevitesse = models.CharField(max_length=50, null=True, blank=True)
    nbrplaces = models.PositiveIntegerField(null=True, blank=True)


    imageproprio = models.ImageField(upload_to="",null=True,blank=True)
    nom=models.CharField(max_length=20,null=True,blank=True)
    telephone=models.IntegerField(null=True,blank=True)
    email=models.EmailField(max_length=50,null=True,blank=True)
    prix= models.CharField(max_length=10,null=True,blank=True)
    cartegrise=models.FileField(upload_to=" ",null=True,blank=True,default=False)
    content=models.TextField(max_length=100,null=True,blank=True)



    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)

    def __str__(self):
     return self.marque




