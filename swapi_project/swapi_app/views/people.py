import petl as etl
from django.views import View
from django.http import HttpResponse


from swapi_app.connectors.people_connector import SwapiPeopleConnector
from swapi_app.converters.converter import TableConverter, HEADER


class PeopleView(View):
    def get(self, request):
        table = etl.setheader(SwapiPeopleConnector().fetch_people(), HEADER)
        converted_table = TableConverter().convert_table(table)
        return HttpResponse(converted_table)
