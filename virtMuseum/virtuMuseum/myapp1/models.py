from django.db import models
class gorodaGeroi(models.Model):
    objects = None
    rankGeroi=models.CharField(max_length=30, blank=True)
    nameGeroi = models.CharField(max_length=30, blank=True)
    smallGeroi = models.CharField(max_length=10000, blank=True)
    bigGeroi=models.CharField(max_length=10000, blank=True)
    longGeroi=models.DecimalField(max_digits=9, decimal_places=6)
    latGeroi = models.DecimalField(max_digits=9, decimal_places=6)
    def __str__(self):
        return self.nameGeroi

class gorodaSlavi(models.Model):
    objects = None
    rankSlavi = models.CharField(max_length=30, blank=True)
    nameSlavi = models.CharField(max_length=30, blank=True)
    smallSlavi = models.CharField(max_length=10000, blank=True)
    bigSlavi = models.CharField(max_length=10000, blank=True)
    longSlavi = models.DecimalField(max_digits=9, decimal_places=6)
    latSlavi = models.DecimalField(max_digits=9, decimal_places=6)
    def __str__(self):
        return self.nameSlavi

class gorodaDoblesti(models.Model):
    objects = None
    rankDoblesti = models.CharField(max_length=30, blank=True)
    nameDoblesti = models.CharField(max_length=30, blank=True)
    smallDoblesti = models.CharField(max_length=10000, blank=True)
    bigDoblesti = models.CharField(max_length=10000, blank=True)
    longDoblesti = models.DecimalField(max_digits=9, decimal_places=6)
    latDoblesti = models.DecimalField(max_digits=9, decimal_places=6)
    def __str__(self):
        return self.nameDoblesti
# Create your models here.
