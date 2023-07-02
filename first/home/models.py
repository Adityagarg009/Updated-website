from django.db import models

# Create your models here.
class Sign(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=20)
    address = models.CharField(max_length=200)
    address2 = models.CharField(max_length=200)
    city = models.CharField(max_length=150)
    state = models.CharField(max_length=20)
    phone = models.CharField(max_length=12)
    date = models.DateField()