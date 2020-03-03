from django.db import models
from account.models import Account
# Create your models here.


class Province(models.Model):
    province = models.CharField(max_length = 100)

    def __str__(self):
        return self.province


class District(models.Model):
    province = models.ForeignKey(Province, on_delete=models.CASCADE)
    district = models.CharField(max_length=100)

    def __str__(self):
        return self.district


class Sector(models.Model):
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    sector = models.CharField(max_length= 100)

    def __str__(self):
        return self.sector


class Cell(models.Model):
    sector = models.ForeignKey(Sector, on_delete=models.CASCADE)
    cell = models.CharField(max_length= 100)

    def __str__(self):
        return self.cell


class Village(models.Model):
    cell = models.ForeignKey(Cell, on_delete=models.CASCADE)
    village = models.CharField(max_length= 100)

    def __str__(self):
        return self.village


class Addresses(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    province = models.ForeignKey(Province, on_delete=models.CASCADE)
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    sector = models.ForeignKey(Sector, on_delete=models.CASCADE)
    cell = models.ForeignKey(Cell, on_delete=models.CASCADE)
    village = models.ForeignKey(Village, on_delete=models.CASCADE)
    street_address = models.CharField(max_length=50)