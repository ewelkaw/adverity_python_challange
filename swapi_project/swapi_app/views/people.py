from django.views import View


class PeopleView(View):
    def get(self, request):
        response = request.get("https://swapi.dev/api/people/")
        # response["results"][0]["homeworld"]
        return response.json()
