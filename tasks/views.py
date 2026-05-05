from django.shortcuts import render

def index(request):
    return render(request, "index.html")


def integrity_dashboard(request):

    files_data = [

        {
            "file": "app.exe",
            "status": "OK",
            "reason": "Целостность подтверждена"
        },

        {
            "file": "config.cfg",
            "status": "MODIFIED",
            "reason": "Обнаружена подмена"
        },
        

        {
            "file": "lib.dll",
            "status": "MODIFIED",
            "reason": "Изменение библиотеки"
        },

        {
            "file": "driver.sys",
            "status": "OK",
            "reason": "Целостность подтверждена"
        },

        {
            "file": "unknown.bin",
            "status": "UNKNOWN",
            "reason": "Файл отсутствует в базе"
        }
    ]

    ok_count = 0
    modified_count = 0
    unknown_count = 0

    for item in files_data:

        if item["status"] == "OK":
            ok_count += 1

        elif item["status"] == "MODIFIED":
            modified_count += 1

        else:
            unknown_count += 1

    context = {

        "files": files_data,

        "ok_count": ok_count,

        "modified_count": modified_count,

        "unknown_count": unknown_count
    }

    return render(request, "integrity_dashboard.html", context)