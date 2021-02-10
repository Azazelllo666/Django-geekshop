from django.contrib import admin
from mainapp.models import ProductCategory, Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'quantity')
    fields = ('name', 'image', 'description', 'short_description', ('price', 'quantity'), 'category')
    readonly_fields = ('price',)
    ordering = ('-quantity',)
    search_fields = ('name', 'category__name')


@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    readonly_fields = ('name',)
    search_fields = ('name',)
