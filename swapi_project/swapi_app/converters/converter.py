import petl as etl
from petl import dateparser
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
            SwapiPlanetsConnector().fetch_planets(), ["homeworld", "url"]
        )

        return (
            people_table.join(planets_table, lkey="homeworld", rkey="url")
            .cutout("homeworld")
            .movefield("edited", 9)
            .rename("edited", "date")
            .convert("date", dateparser("%Y-%m-%dT%H:%M:%S.%f%z"))
        )
