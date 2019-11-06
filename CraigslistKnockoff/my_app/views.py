import requests
from django.shortcuts import render
from bs4 import BeautifulSoup

def home(request):
    return render(request, 'my_app/base.html')

def new_search(request):
    search = request.GET.get('search_text')
    results = {
        'search': search
    }
    return render(request, 'my_app/new_search.html', results)
