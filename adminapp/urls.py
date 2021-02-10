from django.urls import path
import adminapp.views as adminapp


app_name = 'adminapp'

urlpatterns = [
    path('', adminapp.index, name='index'),
    path('admin-users-read/', adminapp.admin_users_read, name='admin_users_read'),
    path('admin-users-create/', adminapp.admin_users_create, name='admin_users_create'),
    path('admin-users-update/<int:id>/', adminapp.admin_users_update, name='admin_users_update'),
    path('admin-users-delete/<int:id>/', adminapp.admin_users_delete, name='admin_users_delete'),
    path('admin-products-read/', adminapp.admin_products_read, name='admin_products_read'),
    path('admin-products-create/', adminapp.admin_products_create, name='admin_products_create'),
    path('admin-products-update/<int:id>/', adminapp.admin_products_update, name='admin_products_update'),
    path('admin-products-delete/<int:id>/', adminapp.admin_products_delete, name='admin_products_delete'),
]
