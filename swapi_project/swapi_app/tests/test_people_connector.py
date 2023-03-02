from django.test import TestCase
from swapi_app.connectors.people_connector import SwapiPeopleConnector

# Create your tests here.

EXPECTED_DATA = [
    [
        "Luke Skywalker",
        "172",
        "77",
        "blond",
        "fair",
        "blue",
        "19BBY",
        "male",
        "https://swapi.dev/api/planets/1/",
        "2014-12-20T21:17:56.891000Z",
    ],
    [
        "C-3PO",
        "167",
        "75",
        "n/a",
        "gold",
        "yellow",
        "112BBY",
        "n/a",
        "https://swapi.dev/api/planets/1/",
        "2014-12-20T21:17:50.309000Z",
    ],
    [
        "Luke Skywalker",
        "172",
        "77",
        "blond",
        "fair",
        "blue",
        "19BBY",
        "male",
        "https://swapi.dev/api/planets/1/",
        "2014-12-20T21:17:56.891000Z",
    ],
    [
        "C-3P1",
        "167",
        "75",
        "n/a",
        "gold",
        "yellow",
        "112BBY",
        "n/a",
        "https://swapi.dev/api/planets/1/",
        "2014-12-20T21:17:50.309000Z",
    ],
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
                        "name": "Luke Skywalker",
                        "height": "172",
                        "mass": "77",
                        "hair_color": "blond",
                        "skin_color": "fair",
                        "eye_color": "blue",
                        "birth_year": "19BBY",
                        "gender": "male",
                        "homeworld": "https://swapi.dev/api/planets/1/",
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
                        "homeworld": "https://swapi.dev/api/planets/1/",
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
                ],
            },
            {
                "next": None,
                "results": [
                    {
                        "name": "Luke Skywalker",
                        "height": "172",
                        "mass": "77",
                        "hair_color": "blond",
                        "skin_color": "fair",
                        "eye_color": "blue",
                        "birth_year": "19BBY",
                        "gender": "male",
                        "homeworld": "https://swapi.dev/api/planets/1/",
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
                        "name": "C-3P1",
                        "height": "167",
                        "mass": "75",
                        "hair_color": "n/a",
                        "skin_color": "gold",
                        "eye_color": "yellow",
                        "birth_year": "112BBY",
                        "gender": "n/a",
                        "homeworld": "https://swapi.dev/api/planets/1/",
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
                ],
            },
        ]
        return data[self.call_count]


class PeopleRequestMock:
    def __init__(self):
        self.call_count = 0

    def get(self, _):
        response = Response(self.call_count)
        self.call_count += 1
        return response


class SwapiPeoppeConnectorTest(TestCase):
    def test_swapi_people_connector(self):
        response = SwapiPeopleConnector(PeopleRequestMock()).fetch_data()
        self.assertEqual(list(response), EXPECTED_DATA)
