from django.test import Client
from django.test import TestCase


class SwapiTablesViewTest(TestCase):
    def test_get_method_in_swapi_tables_view(self):
        response = Client().get("/")
        self.assertEqual(response.status_code, 200)

    def test_post_method_in_swapi_tables_view(self):
        response = Client(enforce_csrf_checks=True).post("/")
        self.assertEqual(response.status_code, 403)
