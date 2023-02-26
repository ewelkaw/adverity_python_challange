import petl as etl
from django.views import View
from django.http import HttpResponse


from swapi_app.generators.people_generator import SwapiPeopleConnector


class PeopleView(View):
    def get(self, request):
        table = SwapiPeopleConnector().fetch_people()
        print(list(table))
        etl.tocsv(table, "example.csv")
        return HttpResponse("OK")
