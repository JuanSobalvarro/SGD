from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

import datetime


def home(request):

    if request.method == 'POST':
        return render(request, 'core_application/home.html')

    elif request.method == 'GET':
        return render(request, 'core_application/home.html')

    return render(request, 'core_application/home.html')


def search_api(request):
    query = request.GET.get('search', '')
    filter = request.GET.get('filter', '')
    results = []

    all_results = [
        {'title': 'Adilia', 'alias': 'Quesillolover', 'image': 'static/img/instagram.png', 'link': '/adilia', 'type': 'player'},
        {'title': 'Carlos', 'alias': 'monki', 'image': 'static/img/instagram.png', 'link': '/adilia', 'type': 'player'},
        {'title': 'Satoru', 'alias': 'El mejor de todos', 'image': 'static/img/logo_ulsa.png', 'link': '/satoru', 'type': 'player'},
        {'title': 'Enchiladita', 'alias': 'Los mas enchilados', 'image': 'static/img/github.png', 'link': '/result4', 'type': 'team'},
        {'title': 'c', 'alias': 'alias 3', 'image': 'static/img/facebook.png', 'link': '/result4', 'type': 'tournament'},
        {'title': 'c', 'alias': 'alias 3', 'image': 'static/img/github.png', 'link': '/result4', 'type': 'tournament'},
    ]

    if query:
        """
        Filtering results where the title contains the query string and the type is the 
        same as the filter or the filter is 'all' 
        """
        results = [result for result in all_results if (query.lower() in result['title'].lower() and (result['type'] == filter or filter == 'all'))]

    return JsonResponse({'results': results})
