from django.db import models
class gorodaGeroi(models.Model):
    objects = None
    name = models.CharField(max_length=30, blank=False)
    infa = models.CharField(max_length=10000, blank=False)

    def __str__(self):
        return self.name
# Create your models here.
