import petl as etl
from django.shortcuts import render
from django.views import View

from swapi_app.models.swapi_data_record import SwapiDataRecord


class SwapiSingleTableView(View):
    template_name = "single_table.html"

    def get(self, request, id):
        page = int(request.GET.get("page", 1))
        table_record = SwapiDataRecord.objects.get(pk=id)
        table = etl.fromcsv(table_record.csv_file).head(page * 10)
        table = [list(x) for x in table]
        # note - it may display one extra link
        # in case when number of records is divisible by 10
        # but in sake of simplicity and not breaking with huge amount
        # of (which would be the problem in case of counting records)
        next_page_validator = len(table) == (page * 10) + 1  # header

        context = {
            "file_name": table_record.csv_file.name.strip("static/"),
            "table": table,
            "id": id,
            "next_page": page + 1 if next_page_validator else 0,
            "page": page,
        }
        return render(request, self.template_name, context)
