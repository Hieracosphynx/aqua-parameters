from django.db import models
from django.contrib.auth.models import User
# Create your models here.
import os


class Tank(models.Model):
    owner_id = models.ForeignKey(User, on_delete=models.CASCADE)
    alias = models.CharField(max_length=100)
    gallons = models.DecimalField(max_digits=5, decimal_places=2)

    class Meta:
        ordering = ['alias']
        verbose_name_plural = "Tanks"

    def __str__(self):
        return self.alias

class Fertilizer(models.Model):
    brand = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    tank_id = models.ForeignKey(Tank, on_delete=models.CASCADE)

    class Meta:
        ordering = ['type']
        verbose_name_plural = "Fertilizers"

    def __str__(self):
        return os.path.join(self.type, ' ', str(self.tank_id))

