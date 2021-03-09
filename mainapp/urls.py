from django.urls import path, re_path
import mainapp.views as mainapp


app_name = 'mainapp'

urlpatterns = [
    re_path(r'^$', mainapp.products, name='index'),
    re_path(r'^(?P<category_id>\d+)/$', mainapp.products, name='product'),
    re_path(r'^page/(?P<page>\d+)/$', mainapp.products, name='page'),
    # TODO: Доделать, чтобы листалось по категориям.
    # re_path(r'^(?P<page>\d+)/(?P<page>\d+)/$', mainapp.products, name='page'),
    # path('<int:category_id>/<int:page>/', mainapp.products, name='page_category')
]
