from django.db import models


# Create your models here.


class Citizen(models.Model):
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    father_name = models.CharField(max_length=255)
    mother_name = models.CharField(max_length=255)
    phone_number = models.IntegerField()
    email = models.EmailField()
    nationality = models.CharField(max_length=100)
    identification = models.IntegerField()
    date_of_birth = models.DateField()
    place_of_birth = models.CharField(max_length=100)
    sex = models.BooleanField()























