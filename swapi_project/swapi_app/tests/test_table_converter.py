import datetime

import petl as etl
from django.test import TestCase

from swapi_app.converters.converter import HEADER, TableConverter

EXPECTED_DATA = [
    (
        "Luke Skywalker",
        "172",
        77,
        "blond",
        "fair",
        "blue",
        "19BBY",
        "male",
        "Alderaan",
        datetime.date(2014, 12, 20),
    ),
    (
        "C-3PO",
        "167",
        75,
        "n/a",
        "gold",
        "yellow",
        "112BBY",
        "n/a",
        "Alderaan",
        datetime.date(2014, 12, 20),
    ),
]

PLANETS_DATA = [
    {"homeworld": "Alderaan", "url": "https://swapi.dev/api/planets/2/"},
    {"homeworld": "Yavin IV", "url": "https://swapi.dev/api/planets/3/"},
    {"homeworld": "Hoth", "url": "https://swapi.dev/api/planets/4/"},
    {"homeworld": "Dagobah", "url": "https://swapi.dev/api/planets/5/"},
    {"homeworld": "Bespin", "url": "https://swapi.dev/api/planets/6/"},
]
PEOPLE_DATA = [
    {
        "name": "Luke Skywalker",
        "height": "172",
        "mass": "77",
        "hair_color": "blond",
        "skin_color": "fair",
        "eye_color": "blue",
        "birth_year": "19BBY",
        "gender": "male",
        "homeworld": "https://swapi.dev/api/planets/2/",
        "films": [
            "https://swapi.dev/api/films/1/",
            "https://swapi.dev/api/films/2/",
            "https://swapi.dev/api/films/3/",
            "https://swapi.dev/api/films/6/",
        ],
        "species": [],
        "vehicles": [
            "https://swapi.dev/api/vehicles/14/",
            "https://swapi.dev/api/vehicles/30/",
        ],
        "starships": [
            "https://swapi.dev/api/starships/12/",
            "https://swapi.dev/api/starships/22/",
        ],
        "created": "2014-12-09T13:50:51.644000Z",
        "edited": "2014-12-20T21:17:56.891000Z",
        "url": "https://swapi.dev/api/people/1/",
    },
    {
        "name": "C-3PO",
        "height": "167",
        "mass": "75",
        "hair_color": "n/a",
        "skin_color": "gold",
        "eye_color": "yellow",
        "birth_year": "112BBY",
        "gender": "n/a",
        "homeworld": "https://swapi.dev/api/planets/2/",
        "films": [
            "https://swapi.dev/api/films/1/",
            "https://swapi.dev/api/films/2/",
            "https://swapi.dev/api/films/3/",
            "https://swapi.dev/api/films/4/",
            "https://swapi.dev/api/films/5/",
            "https://swapi.dev/api/films/6/",
        ],
        "species": ["https://swapi.dev/api/species/2/"],
        "vehicles": [],
        "starships": [],
        "created": "2014-12-10T15:10:51.357000Z",
        "edited": "2014-12-20T21:17:50.309000Z",
        "url": "https://swapi.dev/api/people/2/",
    },
]


class SwapiPlanetsConnectorMock:
    def __init__(self, _):
        pass

    def fetch_data(self):
        return etl.fromdicts(PLANETS_DATA)


class ConverterTest(TestCase):
    def test_table_converter(self):
        table = etl.fromdicts(
            map(lambda x: {name: x[name] for name in HEADER}, PEOPLE_DATA)
        )
        converted_table = TableConverter(SwapiPlanetsConnectorMock).convert_table(table)

        self.assertEqual(list(etl.util.base.data(converted_table)), EXPECTED_DATA)
