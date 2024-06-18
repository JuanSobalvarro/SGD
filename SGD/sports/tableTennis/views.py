from django.shortcuts import render


def tableTennisHome(request):
    return render(request, 'tableTennis/tableTennis_home.html')
