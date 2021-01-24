import json

from django.shortcuts import render


def index(request):
    context = {
        'title': 'Главная - GeekShop'
    }
    return render(request, 'mainapp/index.html', context)


def products(request):
    with open('mainapp/fixtures/city.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
        cities = []
        for city in data:
            cities.append(city['city'])

    context = {
        'title': 'Каталог - GeekShop',
        'cities_json': cities,
        'products': [
            {'name': 'Худи черного цвета с монограммами adidas Originals',
             'price': '6 090,00',
             'text': 'Мягкая ткань для свитшотов. Стиль и комфорт – это образ жизни.',
             'src': 'vendor/img/products/Adidas-hoodie.png'},
            {'name': 'Синяя куртка The North Face',
             'price': '23 725,00',
             'text': 'Гладкая ткань. Водонепроницаемое покрытие. Легкий и теплый пуховый наполнитель.',
             'src': 'vendor/img/products/Blue-jacket-The-North-Face.png'},
            {'name': 'Коричневый спортивный oversized-топ ASOS DESIGN',
             'price': '3 390,00',
             'text': 'Материал с плюшевой текстурой. Удобный и мягкий.',
             'src': 'vendor/img/products/Brown-sports-oversized-top-ASOS-DESIGN.png'},
            {'name': 'Черный рюкзак Nike Heritage',
             'price': '2 340,00',
             'text': 'Плотная ткань. Легкий материал.',
             'src': 'vendor/img/products/Black-Nike-Heritage-backpack.png'},
            {'name': 'Черные туфли на платформе с 3 парами люверсов Dr Martens 1461 Bex',
             'price': '13 590,00',
             'text': 'Гладкий кожаный верх. Натуральный материал.',
             'src': 'vendor/img/products/Black-Dr-Martens-shoes.png'},
            {'name': 'Темно-синие широкие строгие брюки ASOS DESIGN',
             'price': '2 890,00',
             'text': 'Легкая эластичная ткань сирсакер Фактурная ткань.',
             'src': 'vendor/img/products/Dark-blue-wide-leg-ASOs-DESIGN-trousers.png'}
        ]
    }
    return render(request, 'mainapp/products.html', context)
