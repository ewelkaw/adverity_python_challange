from django.test import TestCase
from swapi_app.connectors.people_connector import SwapiPeopleConnector
from swapi_app.connectors.planets_connector import SwapiPlanetsConnector

# Create your tests here.


def test_swapi_people_connector():
    assert SwapiPeopleConnector("link", RequestMock()).make_request() == "link"
