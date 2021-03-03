from django.urls import path, re_path
import basket.views as basket

app_name = 'baskets'

urlpatterns = [
    re_path(r'^basket-add/(?P<product_id>\d+)/$', basket.basket_add, name='basket_add'),
    re_path(r'^basket-remove/(?P<id>\d+)/$', basket.basket_remove, name='basket_remove'),
    re_path(r'^edit/(?P<id>\d+)/(?P<quantity>\d+)/$', basket.basket_edit, name='basket_edit'),
]
