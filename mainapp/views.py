import json
from django.shortcuts import render
from mainapp.models import ProductCategory, Product


def index(request):
    context = {
        'title': 'Главная - GeekShop'
    }
    return render(request, 'mainapp/index.html', context)


def products(request, pk=None):
    print(pk)

    with open('mainapp/fixtures/city.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
        cities = []
        for city in data:
            cities.append(city['city'])

    context = {
        'title': 'Каталог - GeekShop',
        'products': Product.objects.all(),
        'categories': ProductCategory.objects.all(),
        'cities_json': cities
    }
    return render(request, 'mainapp/products.html', context)
