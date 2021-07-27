from django.db import models

# Create your models here.


class Dealer(models.Model):
    name = models.CharField(max_length=10, verbose_name='Dealer name')


class Car(models.Model):
    brand = models.CharField(max_length=10, verbose_name="Car's brand")
    model = models.CharField(max_length=10, verbose_name="Car's model")
    dealer = models.ForeignKey('Dealer', on_delete=models.CASCADE, verbose_name="Car's dealer")