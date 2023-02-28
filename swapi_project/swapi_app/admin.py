from django.contrib import admin

# Register your models here.
from .models.people import PeopleTable

admin.site.register(PeopleTable)
