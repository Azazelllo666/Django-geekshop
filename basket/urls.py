from django.urls import path
import basket.views as basket

app_name = 'baskets'

urlpatterns = [
    path('basket-add/<int:product_id>/', basket.basket_add, name='basket_add'),
    path('basket-remove/<int:id>/', basket.basket_remove, name='basket_remove'),
    path('edit/<int:id>/<int:quantity>/', basket.basket_edit, name='basket_edit'),
]
