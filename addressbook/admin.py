from django.contrib import admin
from .models import Province, District, Sector, Cell, Village
# Register your models here.
admin.site.register(Province)
admin.site.register(District)
admin.site.register(Sector)
admin.site.register(Cell)
admin.site.register(Village)