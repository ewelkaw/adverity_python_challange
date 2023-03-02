from django.test import TestCase
from swapi_app.connectors.planets_connector import SwapiPlanetsConnector

# Create your tests here.

EXPECTED_DATA = [
    ["Tatooine", "https://swapi.dev/api/planets/1/"],
    ["Alderaan", "https://swapi.dev/api/planets/2/"],
    ["Yavin IV", "https://swapi.dev/api/planets/3/"],
    ["Tatooine", "https://swapi.dev/api/planets/1/"],
    ["Yavin IV", "https://swapi.dev/api/planets/3/"],
]


class Response:
    def __init__(self, call_count):
        self.call_count = call_count

    def json(self):
        data = [
            {
                "next": "next",
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
            },
            {
                "next": "next",
                "results": [
                    {
                        "name": "Tatooine",
                        "rotation_period": "23",
                        "url": "https://swapi.dev/api/planets/1/",
                    },
                ],
            },
            {
                "next": None,
                "results": [
                    {
                        "name": "Yavin IV",
                        "rotation_period": "24",
                        "url": "https://swapi.dev/api/planets/3/",
                    },
                ],
            },
        ]
        return data[self.call_count]


class PlanetsRequestMock:
    def __init__(self):
        self.counter = 0

    def get(self, _):
        response = Response(self.counter)
        self.counter += 1
        return response


class SwapiPlanetsConnectorTest(TestCase):
    def test_swapi_people_connector(self):
        response = SwapiPlanetsConnector(PlanetsRequestMock()).fetch_data()
        self.assertEqual(list(response), EXPECTED_DATA)
