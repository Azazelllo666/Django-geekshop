from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import user_passes_test

from authapp.models import User
from adminapp.forms import UserAdminRegisterForm, UserAdminProfileForm, ProductAdminCreateForm, ProductAdminUpdateForm
from mainapp.models import Product


@user_passes_test(lambda u: u.is_superuser, login_url='/')
def index(request):
    return render(request, 'adminapp/index.html')


@user_passes_test(lambda u: u.is_superuser, login_url='/')
def admin_users_read(request):
    users = User.objects.all()
    context = {
        'users': users
    }
    return render(request, 'adminapp/admin-users-read.html', context)


@user_passes_test(lambda u: u.is_superuser, login_url='/')
def admin_users_create(request):
    if request.method == 'POST':
        form = UserAdminRegisterForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admins:admin_users_read'))
    else:
        form = UserAdminRegisterForm()
    context = {
        'title': 'GeekShop - Регистрация',
        'form': form,
    }
    return render(request, 'adminapp/admin-users-create.html', context)


@user_passes_test(lambda u: u.is_superuser, login_url='/')
def admin_users_update(request, id):
    user = User.objects.get(id=id)
    if request.method == 'POST':
        form = UserAdminProfileForm(data=request.POST, files=request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admins:admin_users_read'))
    else:
        form = UserAdminProfileForm(instance=user)
    context = {
        'form': form,
        'current_user': user,
    }
    return render(request, 'adminapp/admin-users-update.html', context)


@user_passes_test(lambda u: u.is_superuser, login_url='/')
def admin_users_delete(request, id):
    user = User.objects.get(id=id)
    user.is_active = False
    user.save()
    return HttpResponseRedirect(reverse('admins:admin_users_read'))


@user_passes_test(lambda u: u.is_superuser, login_url='/')
def admin_products_read(request):
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request, 'adminapp/admin-products-read.html', context)


@user_passes_test(lambda u: u.is_superuser, login_url='/')
def admin_products_create(request):
    if request.method == 'POST':
        form = ProductAdminCreateForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admins:admin_products_read'))
    else:
        form = ProductAdminCreateForm()
    context = {
        'form': form,
    }
    return render(request, 'adminapp/admin-products-create.html', context)


@user_passes_test(lambda u: u.is_superuser, login_url='/')
def admin_products_update(request, id):
    product = Product.objects.get(id=id)
    if request.method == 'POST':
        form = ProductAdminUpdateForm(data=request.POST, files=request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admins:admin_products_read'))
    else:
        form = ProductAdminUpdateForm(instance=product)
    context = {
        'form': form,
        'current_product': product,
    }
    return render(request, 'adminapp/admin-products-update-delete.html', context)


@user_passes_test(lambda u: u.is_superuser, login_url='/')
def admin_products_delete(request, id):
    product = Product.objects.get(id=id)
    product.quantity = 0
    product.save()
    return HttpResponseRedirect(reverse('admins:admin_products_read'))