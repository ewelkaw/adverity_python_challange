import requests


class SwapiPeopleConnector:
    next_page = "https://swapi.dev/api/people/"

    def fetch_people(self):
        while self.next_page:
            response = requests.get(self.next_page)
            results = response.json()
            proper_results = results["results"]
            table = [[proper_results[0].keys()]]
            for i in proper_results:
                table.extend(i.values())
            yield table
            self.next_page = results.get("next")
