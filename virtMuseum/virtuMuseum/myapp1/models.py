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
# Create your models here.
