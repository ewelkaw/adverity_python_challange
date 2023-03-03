from urllib.parse import urlencode

import petl as etl
from django.shortcuts import render
from django.views import View

from swapi_app.models.swapi_data_record import SwapiDataRecord


class ValuesCountTableView(View):
    template_name = "values_count.html"

    def get(self, request, id):
        page = int(request.GET.get("page", 1))
        table_record = SwapiDataRecord.objects.get(pk=id)
        table = etl.fromcsv(table_record.csv_file).head(page * 10)

        header = list(etl.header(table))
        header_filter = list(map(lambda h: (h, request.GET.get(h, ["0"])[-1]), header))
        if columns := tuple((x[0] for x in header_filter if x[1] == "1")):
            table = etl.valuecounts(table, *columns).cutout("frequency")
            # counting values based on loaded data on previous page
            # as it wasn't clarified in specification
        table = [list(x) for x in table]

        context = {
            "file_name": table_record.csv_file.name.strip("static/"),
            "table": table,
            "id": id,
            "header_filter": header_filter,
            "page": page,
            "links": urlencode(header_filter),
        }
        return render(request, self.template_name, context)
