from django.http import HttpResponse
from xlwt import Workbook


def get_xls_file(queryset):
    result_dict = dict()

    for model, index in queryset:
        result_dict.setdefault(model, dict())
        result_dict[model].setdefault(index, 0)
        result_dict[model][index] += 1

    workbook = Workbook()

    for mod, mod_dict in result_dict.items():
        sheet = workbook.add_sheet("Model {}".format(mod))
        columns = ["Модель", "Версия", "Количество за неделю"]

        for col_num, header in enumerate(columns):
            sheet.write(0, col_num, header)

        for ind_ver, (ver, count) in enumerate(mod_dict.items(), start=1):
            sheet.write(ind_ver, 0, mod)
            sheet.write(ind_ver, 1, ver)
            sheet.write(ind_ver, 2, count)

    response = HttpResponse(content_type="application/vnd.ms-excel")
    response["Content-Disposition"] = "attachment; filename=data.xls"
    workbook.save(response)
    return response
