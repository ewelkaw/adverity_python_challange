import uuid
import tempfile
import petl as etl
from django.core.files import File
from swapi_app.models.people import PeopleTable


def create_new_record(converted_table):
    tmp_file = tempfile.NamedTemporaryFile(
        suffix=".csv",
    )

    etl.tocsv(converted_table, tmp_file.name)
    people = PeopleTable.objects.create()

    with open(tmp_file.name, "rb") as people_file:
        people.csv_file.save(f"{uuid.uuid4()}.csv", File(people_file), save=True)
    people.save()
