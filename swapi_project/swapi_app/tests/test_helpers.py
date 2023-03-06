import petl as etl
from django.test import TestCase
from swapi_app.helpers import create_new_record
from swapi_app.models.swapi_data_record import SwapiDataRecord


class SwapiTablesViewTest(TestCase):
    header = ["foo", "bar"]
    columns = [["0", "1", "2"], ["a", "b", "c"]]

    def setUp(self) -> None:
        table = etl.fromcolumns(self.columns, header=self.header)
        for _ in range(5):
            create_new_record(table)
        return super().setUp()

    def test_get_all_swapi_data_records_after_creating_them_in_helper(self):
        all_records = SwapiDataRecord.objects.all()
        self.assertEqual(all_records.count(), 5)
        for record in all_records:
            table = etl.fromcsv(record.csv_file)
            self.assertEqual(list(table.values(self.header[0])), self.columns[0])
            self.assertEqual(list(table.values(self.header[1])), self.columns[1])
