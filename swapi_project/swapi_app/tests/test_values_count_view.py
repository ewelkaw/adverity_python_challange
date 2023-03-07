import petl as etl
from django.test import Client
from django.test import TestCase
from swapi_app.helpers import create_new_record
from swapi_app.models.swapi_data_record import SwapiDataRecord


class SwapiValuesCountViewTest(TestCase):
    columns = [["0", "1", "2"], ["a", "b", "c"]]

    def setUp(self) -> None:
        table = etl.fromcolumns(self.columns)
        create_new_record(table)
        return super().setUp()

    def test_get_method_in_values_count_view(self):
        all_records = SwapiDataRecord.objects.all()
        page = 1
        response = Client().get(
            f"/single_table/{all_records.first().pk}/values_count/?page={page}&name=1&height=1&mass=1&hair_color=1&skin_color=1&eye_color=1&birth_year=1&gender=1&homeworld=1&date=0&date=1"
        )
        table = [list(x) for x in zip(*self.columns)]
        table.insert(0, ["f0", "f1"])
        self.assertEqual(response.status_code, 200)
        self.assertEqual(all_records.count(), 1)
        self.assertEqual(
            response.context["file_name"],
            all_records.first().csv_file.name.split("/")[1],
        )
        self.assertEqual(
            response.context["table"],
            table,
        )
        self.assertEqual(response.context["header_filter"], [("f0", "0"), ("f1", "0")])
        self.assertEqual(response.context["page"], page)
