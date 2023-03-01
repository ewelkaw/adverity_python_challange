from django.test import TestCase
from swapi_app.connectors.planets_connector import SwapiPlanetsConnector

# Create your tests here.

EXPECTED_DATA = [
    ["Tatooine", "https://swapi.dev/api/planets/1/"],
    ["Alderaan", "https://swapi.dev/api/planets/2/"],
    ["Yavin IV", "https://swapi.dev/api/planets/3/"],
]


class Response:
    def json(self):
        return {
            "next": None,
            "results": [
                {
                    "name": "Tatooine",
                    "rotation_period": "23",
                    "url": "https://swapi.dev/api/planets/1/",
                },
                {
                    "name": "Alderaan",
                    "rotation_period": "24",
                    "url": "https://swapi.dev/api/planets/2/",
                },
                {
                    "name": "Yavin IV",
                    "rotation_period": "24",
                    "url": "https://swapi.dev/api/planets/3/",
                },
            ],
        }


class PlanetsRequestMock:
    def get(self, _):
        return Response()


class SwapiPlanetsConnectorTest(TestCase):
    def test_swapi_people_connector(self):
        print(SwapiPlanetsConnector(PlanetsRequestMock()).fetch_data())
        response = SwapiPlanetsConnector(PlanetsRequestMock()).fetch_data()
        self.assertEqual(list(response), EXPECTED_DATA)
