import uuid
import tempfile
import petl as etl
from django.core.files import File
from swapi_app.models.swapi_data_record import SwapiDataRecord


def create_new_record(converted_table):
    tmp_file = tempfile.NamedTemporaryFile(
        suffix=".csv",
    )

    etl.tocsv(converted_table, tmp_file.name)
    people = SwapiDataRecord.objects.create()

    with open(tmp_file.name, "rb") as people_file:
        people.csv_file.save(f"{uuid.uuid4()}.csv", File(people_file), save=True)
    people.save()
