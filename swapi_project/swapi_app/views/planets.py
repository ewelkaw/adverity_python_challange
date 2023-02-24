from django.views import View


class PeopleView(View):
    def get(self, request):
        response = request.get("https://swapi.dev/api/planets/")
        # response["results"][0] ["url"],["name"]
        return response.json()
