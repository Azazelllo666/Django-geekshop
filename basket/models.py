from django.db import models
from django.shortcuts import get_object_or_404
from django.utils.functional import cached_property

from mainapp.models import Product
from authapp.models import User


class Basket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='basket')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    created_timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Корзина для {self.user.username} | Продукт {self.product.name}'

    def sum(self):
        return self.quantity * self.product.price

    def total_quantity(self):
        baskets = self.get_items_cached
        return sum(basket.quantity for basket in baskets)

    def total_cost(self):
        baskets = self.get_items_cached
        return sum(basket.sum() for basket in baskets)

    @staticmethod
    def get_items(user):
        return Basket.objects.filter(user=user).order_by("product__category")

    @staticmethod
    def get_item(pk):
        return get_object_or_404(Basket, pk=pk)

    @cached_property
    def get_items_cached(self):
        return self.user.basket.select_related()
