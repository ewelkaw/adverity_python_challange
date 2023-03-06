import petl as etl
from django.test import Client
from django.test import TestCase
from swapi_app.helpers import create_new_record


class SwapiTablesViewTest(TestCase):
    def setUp(self) -> None:
        columns = [[0, 1, 2], ["a", "b", "c"]]
        table = etl.fromcolumns(columns)
        for _ in range(3):
            create_new_record(table)
            # decided to use helper as it was tested in other test file
        return super().setUp()

    def test_get_method_in_swapi_tables_view(self):
        response = Client().get("/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context[0]["elements"].count(), 3)

    def test_post_method_in_swapi_tables_view(self):
        response = Client(enforce_csrf_checks=True).post("/")
        self.assertEqual(response.status_code, 403)
