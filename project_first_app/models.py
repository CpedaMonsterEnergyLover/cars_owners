from django.contrib.auth.models import AbstractUser
from django.db import models


class Car(models.Model):
    number = models.CharField(max_length=15)
    brand = models.CharField(max_length=20)
    model = models.CharField(max_length=20)
    color = models.CharField(max_length=30)


class Owner(AbstractUser):
    first_name = models.CharField(max_length=30)
    second_name = models.CharField(max_length=30)
    birth_date = models.DateTimeField(blank=True, null=True)
    home_address = models.CharField(max_length=60, default='')
    nation = models.CharField(max_length=60, default='')
    passport_number = models.CharField(max_length=10, default='')

    #REQUIRED_FIELDS = ['user_name']


class License(models.Model):
    owner_license = models.ForeignKey(Owner, on_delete=models.CASCADE)
    number = models.CharField(max_length=10)
    type = models.CharField(max_length=10)
    date = models.DateTimeField()


class Ownership(models.Model):
    owner_ownership = models.ForeignKey(Owner, on_delete=models.CASCADE)
    car_ownership = models.ForeignKey(Car, on_delete=models.CASCADE)
    date_start = models.DateTimeField()
    date_ending = models.DateTimeField()


