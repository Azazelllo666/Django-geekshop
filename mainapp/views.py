import json
from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from mainapp.models import ProductCategory, Product


def index(request):
    context = {
        'title': 'Главная - GeekShop'
    }
    return render(request, 'mainapp/index.html', context)


def products(request, category_id=None, page=1):
    if category_id:
        products = Product.objects.filter(category_id=category_id)
    else:
        products = Product.objects.all()
    paginator = Paginator(products.order_by('-price'), per_page=3)
    # products_paginator = paginator.page(page)
    try:
        products_paginator = paginator.page(page)
    except PageNotAnInteger:
        products_paginator = paginator.page(1)
    except EmptyPage:
        products_paginator = paginator.page(paginator.num_pages)

    context = {
        'title': 'Каталог - GeekShop',
        'products': products_paginator,
        'categories': ProductCategory.objects.all(),
    }
    return render(request, 'mainapp/products.html', context)
