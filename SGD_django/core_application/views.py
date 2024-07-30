from django.http import HttpResponse
from django.shortcuts import render
import datetime


def home(request):
    """
    View function for home page
    """
    if request.method == 'POST':
        return render(request, 'core_application/home.html')

    elif request.method == 'GET':
        return render(request, 'core_application/home.html')

    return render(request, 'core_application/home.html')


def about(request):
    """
    View function for about page
    """
    if request.method == 'POST':
        return render(request, 'core_application/about.html')
    elif request.method == 'GET':
        return render(request, 'core_application/about.html')

    return render(request, 'core_application/about.html')