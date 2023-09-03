from django.db import models
from django.contrib.auth.models import User


class Fci(models.Model):
    nombre=models.CharField(max_length=50)
    nomenclatura=models.CharField(max_length=50)
    cuotapartes=models.IntegerField()
    ultimo_valor=models.DecimalField(decimal_places=2, max_digits=50)
    fecha_actualizacion=models.DateField()
    
    def valor_total(self):
        return self.cuotapartes*self.ultimo_valor


   
    def __str__(self):
        return f"{self.nombre}"
    
    class Meta:
        verbose_name="Fondo Común"
        verbose_name_plural="Fondos Comunes"
        ordering=['nombre']
    

class Acciones(models.Model):
    nombre=models.CharField(max_length=50)
    nomenclatura=models.CharField(max_length=50)
    nominales=models.IntegerField()
    fecha_inicio=models.DateField()


    def __str__(self):
        return f"{self.nombre}"
    
    class Meta:
        verbose_name="Acción"
        verbose_name_plural="Acciones"
        ordering=['nombre']


class Bono(models.Model):
    nombre=models.CharField(max_length=50)
    nomenclatura=models.CharField(max_length=50)
    nominales=models.IntegerField()
    ultimo_valor=models.DecimalField(decimal_places=2, max_digits=50)
    fecha_actualizacion=models.DateField()
    
    def valor_total(self):
        return self.nominales*self.ultimo_valor

  

    def __str__(self):
        return f"{self.nombre}"
    
    class Meta:
        verbose_name="Bono"
        verbose_name_plural="Bonos"
        ordering=['nombre']

class Cauciones(models.Model):
    nombre=models.CharField(max_length=50)
    nomenclatura=models.CharField(max_length=50)
    nominales=models.IntegerField()
    ultimo_valor=models.DecimalField(decimal_places=2, max_digits=50)
    fecha_actualizacion=models.DateField()
    
    def valor_total(self):
        return self.nominales*self.ultimo_valor
     




    def __str__(self):
        return f"{self.nombre}"
    
    class Meta:
        verbose_name="Caución"
        verbose_name_plural="Cauciones"
        ordering=['nombre']


class Avatar(models.Model):
    avatar = models.ImageField(upload_to="avatares", null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user} {self.avatar}"
    

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to="avatares", null=True, blank=True)

    def __str__(self):
        return str(self.user)