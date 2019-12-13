from django.contrib import admin
from .models import CommunicationsToCell, CommunicationToDistrict, CommunicationToProvince, CommunicationToSector, CommunicationToVillage
# Register your models here.
admin.site.register(CommunicationToProvince)
admin.site.register(CommunicationToDistrict)
admin.site.register(CommunicationToSector)
admin.site.register(CommunicationsToCell)
admin.site.register(CommunicationToVillage)