import requests
from swapi_app.converters.converter import HEADER


class SwapiPeopleConnector:
    next_page = "https://swapi.dev/api/people/"

    def fetch_data(self):
        while self.next_page:
            response = requests.get(self.next_page)
            parsed_response = response.json()
            yield from map(
                lambda x: [x[name] for name in HEADER], parsed_response["results"]
            )
            self.next_page = parsed_response.get("next")
