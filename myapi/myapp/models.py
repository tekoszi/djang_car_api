from django.db import models

class Car(models.Model):
    id = models.AutoField(primary_key=True)
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    rates_number = models.IntegerField(default=0)
    rates_total= models.IntegerField(default=0)
