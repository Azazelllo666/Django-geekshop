from django.urls import path
import adminapp.views as adminapp


app_name = 'adminapp'

urlpatterns = [
    path('', adminapp.index, name='index'),
    path('admin-users-read/', adminapp.UserListView.as_view(), name='admin_users_read'),
    path('admin-users-create/', adminapp.UserCreateView.as_view(), name='admin_users_create'),
    path('admin-users-update/<int:pk>/', adminapp.UserUpdateView.as_view(), name='admin_users_update'),
    path('admin-users-delete/<int:pk>/', adminapp.UserDeleteView.as_view(), name='admin_users_delete'),
    path('admin-products-read/', adminapp.ProductListView.as_view(), name='admin_products_read'),
    path('admin-products-create/', adminapp.ProductCreateView.as_view(), name='admin_products_create'),
    path('admin-products-update/<int:pk>/', adminapp.ProductUpdateView.as_view(), name='admin_products_update'),
    path('admin-products-delete/<int:pk>/', adminapp.ProductDeleteView.as_view(), name='admin_products_delete'),
    path('admin-categories-read/', adminapp.ProductCategoryListView.as_view(), name='admin_categories_read'),
    path('admin-categories-create/', adminapp.ProductCategoryCreateView.as_view(), name='admin_categories_create'),
    path('admin-categories-update/<int:pk>/', adminapp.ProductCategoryUpdateView.as_view(), name='admin_categories_update'),
    path('admin-categories-delete/<int:pk>/', adminapp.ProductCategoryDeleteView.as_view(), name='admin_categories_delete'),
]
