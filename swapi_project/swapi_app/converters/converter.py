import petl as etl
from petl import dateparser, numparser
from swapi_app.connectors.planets_connector import SwapiPlanetsConnector

HEADER = [
    "name",
    "height",
    "mass",
    "hair_color",
    "skin_color",
    "eye_color",
    "birth_year",
    "gender",
    "homeworld",
    "edited",
]


class TableConverter:
    def convert_table(self, people_table):
        planets_table = etl.setheader(
            SwapiPlanetsConnector().fetch_data(), ["homeworld", "url"]
        )
        return (
            people_table.join(planets_table, lkey="homeworld", rkey="url")
            .cutout("homeworld")
            .movefield("edited", 9)
            .rename("edited", "date")
            .convert("date", dateparser("%Y-%m-%dT%H:%M:%S.%f%z"))
            .convert("mass", int)
        )
        # Decided to leave empty or missing values as they are
        # as there was nothing about it in specification
