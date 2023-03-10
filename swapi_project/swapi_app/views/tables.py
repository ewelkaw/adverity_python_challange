import petl as etl
import requests
from django.shortcuts import redirect, render
from django.views import View

from swapi_app.connectors.people_connector import SwapiPeopleConnector
from swapi_app.converters.converter import HEADER, TableConverter
from swapi_app.helpers import create_new_record
from swapi_app.models.swapi_data_record import SwapiDataRecord


class SwapiTablesView(View):
    template_name = "tables.html"

    def get(self, request):
        context = {
            "elements": SwapiDataRecord.objects.order_by("-date_fetched"),
        }
        return render(request, self.template_name, context)

    def post(self, _):
        table = etl.setheader(SwapiPeopleConnector(requests).fetch_data(), HEADER)
        converted_table = TableConverter().convert_table(table)
        create_new_record(converted_table)
        return redirect("/")
