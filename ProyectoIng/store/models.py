from django.db import models
from location.models import Location
from account.models import Account
from images.models import Image
# Create your models here.
"""Clase Tienda, 
Atributos: [Nombre, descripcion, ubicacion de tienda]"""

class Store(models.Model):
    store_name= models.CharField(max_length=100,null=False,blank=False)
    store_description= models.TextField(null=False,blank=False)
    store_location = models.ForeignKey(Location, on_delete=models.CASCADE)
    store_profile_image = models.ImageField(upload_to='store_profile', null= False,blank= False ,default="profile_img/default.png")
    store_background_image = models.ImageField(upload_to='store_background',null= False, blank= False,default="profile_img/default_background.jpg") 

    def __str__(self):
        return self.store_name

    class Meta():
        verbose_name= "Tienda"
        verbose_name_plural= "Tiendas"

class UsersXStore(models.Model):
    store= models.ForeignKey(Store, on_delete=models.CASCADE)
    user= models.ForeignKey(Account, on_delete=models.CASCADE)

    def __str__(self):
        return self.store.store_name+", "+self.user.email
    
    class Meta():
        verbose_name= "Usuario por Tienda"
        verbose_name_plural= "Usuarios por Tiendas"