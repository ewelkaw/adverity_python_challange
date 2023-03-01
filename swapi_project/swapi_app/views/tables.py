import petl as etl
from django.views import View
from django.shortcuts import render, redirect

from swapi_app.connectors.people_connector import SwapiPeopleConnector
from swapi_app.converters.converter import TableConverter, HEADER
from swapi_app.models.swapi_data_record import SwapiDataRecord
from swapi_app.helpers import create_new_record


class SwapiTablesView(View):
    template_name = "tables.html"

    def get(self, request):
        context = {
            "elements": SwapiDataRecord.objects.order_by("-date_fetched"),
        }
        return render(request, self.template_name, context)

    def post(self, request):
        table = etl.setheader(SwapiPeopleConnector().fetch_data(), HEADER)
        converted_table = TableConverter().convert_table(table)
        create_new_record(converted_table)
        return redirect("/")
