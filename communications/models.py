from django.db import models
from addressbook.models import Province, District, Sector, Cell, Village
from account.models import Account
# Create your models here.


class CommunicationToVillage(models.Model):
    message = models.TextField()
    village = models.ForeignKey(Village, on_delete=models.CASCADE)
    author = models.ForeignKey(Account, on_delete=models.CASCADE)
    pub_date = models.DateTimeField()


class CommunicationsToCell(models.Model):
    message = models.TextField()
    cell = models.ForeignKey(Cell, on_delete=models.CASCADE)
    author = models.ForeignKey(Account, on_delete=models.CASCADE)
    pub_date = models.DateTimeField()


class CommunicationToSector(models.Model):
    message = models.TextField()
    sector = models.ForeignKey(Sector, on_delete=models.CASCADE)
    author = models.ForeignKey(Account, on_delete=models.CASCADE)
    pub_date = models.DateTimeField()


class CommunicationToDistrict(models.Model):
    message = models.TextField()
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    author = models.ForeignKey(Account, on_delete=models.CASCADE)
    pub_date = models.DateTimeField()


class CommunicationToProvince(models.Model):
    message = models.TextField()
    province = models.ForeignKey(Province, on_delete=models.CASCADE)
    author = models.ForeignKey(Account, on_delete=models.CASCADE)
    pub_date = models.DateTimeField()