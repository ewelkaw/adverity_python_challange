import petl as etl
from django.test import Client
from django.test import TestCase
from swapi_app.helpers import create_new_record
from swapi_app.models.swapi_data_record import SwapiDataRecord


class SwapiSingleTableViewTest(TestCase):
    tables_columns = [
        [["0", "1", "2"], ["a", "b", "c"]],
        [["3", "4", "5"], ["d", "e", "f"]],
        [["6", "7", "8"], ["g", "h", "i"]],
    ]
    header = ["foo", "bar"]

    def setUp(self) -> None:
        for columns in self.tables_columns:
            table = etl.fromcolumns(columns, header=self.header)
            create_new_record(table)
        return super().setUp()

    def test_get_method_in_single_table_view(self):
        all_records = SwapiDataRecord.objects.all()
        for idx, record in enumerate(all_records):
            response = Client().get(f"/single_table/{record.pk}")
            self.assertEqual(response.status_code, 200)
            table = [list(x) for x in zip(*self.tables_columns[idx])]
            table.insert(0, self.header)
            self.assertEqual(
                response.context["table"],
                table,
            )
            self.assertEqual(
                response.context["page"],
                1,
            )
            self.assertEqual(
                response.context["next_page"],
                0,
            )
