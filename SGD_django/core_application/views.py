from django.http import HttpResponse
from django.shortcuts import render

import datetime


def home(request):

    if request.method == 'POST':
        return render(request, 'core_application/home.html')

    elif request.method == 'GET':
        return render(request, 'core_application/home.html')

    return render(request, 'core_application/home.html')
