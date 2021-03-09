from basket.models import Basket


def basket_func(request):
    print('context processor basket works')
    basket = []

    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)

    return {
        'basket': basket
    }


