from django.contrib import admin

# Register your models here.
from .models.swapi_data_record import SwapiDataRecord

admin.site.register(SwapiDataRecord)
