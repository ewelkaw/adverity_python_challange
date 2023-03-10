from django.db import models


class SwapiDataRecord(models.Model):
    csv_file = models.FileField(upload_to="static/")
    date_fetched = models.DateTimeField(auto_now_add=True)
