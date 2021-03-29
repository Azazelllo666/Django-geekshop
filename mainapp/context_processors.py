from basket.models import Basket


def basket_func(request):
    basket = []

    if request.user.is_authenticated:
        basket = request.user.basket.select_related()

    return {
        'basket': basket
    }


