from django.db import models
from citizens.models import Citizen
# Create your models here.


class Province(models.Model):
    province = models.CharField(max_length = 100)


class District(models.Model):
    province = models.ForeignKey(Province, on_delete=models.CASCADE)
    district = models.CharField(max_length=100)


class Sector(models.Model):
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    sector = models.CharField(max_length= 100)


class Cell(models.Model):
    sector = models.ForeignKey(Sector, on_delete=models.CASCADE)
    cell = models.CharField(max_length= 100)


class Village(models.Model):
    cell = models.ForeignKey(Cell, on_delete=models.CASCADE)
    village = models.CharField(max_length= 100)


class Addresses(models.Model):
    citizen = models.ForeignKey(Citizen, on_delete=models.CASCADE)
    province = models.ForeignKey(Province, on_delete=models.CASCADE)
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    sector = models.ForeignKey(Sector, on_delete=models.CASCADE)
    cell = models.ForeignKey(Cell, on_delete=models.CASCADE)
    village = models.ForeignKey(Village, on_delete=models.CASCADE)
    street_address = models.CharField(max_length=50)