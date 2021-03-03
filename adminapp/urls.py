from django.urls import path, re_path
import adminapp.views as adminapp


app_name = 'adminapp'

urlpatterns = [
    re_path(r'^$', adminapp.index, name='index'),
    re_path(r'^admin-users-read/$', adminapp.UserListView.as_view(), name='admin_users_read'),
    re_path(r'^admin-users-create/$', adminapp.UserCreateView.as_view(), name='admin_users_create'),
    re_path(r'^admin-users-update/(?P<pk>\d+)/$', adminapp.UserUpdateView.as_view(), name='admin_users_update'),
    re_path(r'^admin-users-delete/(?P<pk>\d+)/$', adminapp.UserDeleteView.as_view(), name='admin_users_delete'),
    re_path(r'^admin-products-read/$', adminapp.ProductListView.as_view(), name='admin_products_read'),
    re_path(r'^admin-products-create/$', adminapp.ProductCreateView.as_view(), name='admin_products_create'),
    re_path(r'^admin-products-update/(?P<pk>\d+)/$', adminapp.ProductUpdateView.as_view(), name='admin_products_update'),
    re_path(r'^admin-products-delete/(?P<pk>\d+)/$', adminapp.ProductDeleteView.as_view(), name='admin_products_delete'),
    re_path(r'^admin-categories-read/$', adminapp.ProductCategoryListView.as_view(), name='admin_categories_read'),
    re_path(r'^admin-categories-create/$', adminapp.ProductCategoryCreateView.as_view(), name='admin_categories_create'),
    re_path(r'^admin-categories-update/(?P<pk>\d+)/$', adminapp.ProductCategoryUpdateView.as_view(), name='admin_categories_update'),
    re_path(r'^admin-categories-delete/(?P<pk>\d+)/$', adminapp.ProductCategoryDeleteView.as_view(), name='admin_categories_delete'),
]
