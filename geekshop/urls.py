"""geekshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from django.conf import settings
from django.conf.urls import include
from django.conf.urls.static import static
from mainapp.views import index

urlpatterns = [
    re_path('admin/', admin.site.urls),
    re_path(r'^$', index, name='index'),
    re_path(r'^products/', include('mainapp.urls', namespace='products')),
    re_path(r'^auth/', include('authapp.urls', namespace='auth')),
    re_path(r'^baskets/', include('basket.urls', namespace='baskets')),
    re_path(r'^admin-staff/', include('adminapp.urls', namespace='admins')),
    path("", include("social_django.urls", namespace="social")),
    re_path(r"^order/", include("ordersapp.urls", namespace="order")),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += [re_path(r"^__debug__/", include(debug_toolbar.urls))]
