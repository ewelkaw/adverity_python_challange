import requests


class SwapiPlanetsConnector:
    next_page = "https://swapi.dev/api/planets/"

    def fetch_planets(self):
        while self.next_page:
            response = requests.get(self.next_page)
            parsed_response = response.json()
            yield from map(
                lambda x: [x[name] for name in ["name", "url"]],
                parsed_response["results"],
            )
            self.next_page = parsed_response.get("next")
