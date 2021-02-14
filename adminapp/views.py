from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.decorators import user_passes_test
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy

from authapp.models import User
from adminapp.forms import UserAdminRegisterForm, UserAdminProfileForm, ProductAdminCreateForm, ProductAdminUpdateForm
from mainapp.models import Product


@user_passes_test(lambda u: u.is_superuser, login_url='/')
def index(request):
    return render(request, 'adminapp/index.html')


class UserListView(ListView):
    model = User
    template_name = 'adminapp/admin-users-read.html'

    @method_decorator(user_passes_test(lambda u: u.is_superuser, login_url='/'))
    def dispatch(self, request, *args, **kwargs):
        return super(UserListView, self).dispatch(request, *args, **kwargs)


class UserCreateView(CreateView):
    model = User
    template_name = 'adminapp/admin-users-create.html'
    form_class = UserAdminRegisterForm
    success_url = reverse_lazy('admins:admin_users_read')

    @method_decorator(user_passes_test(lambda u: u.is_superuser, login_url='/'))
    def dispatch(self, request, *args, **kwargs):
        return super(UserCreateView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(UserCreateView, self).get_context_data(**kwargs)
        context['title'] = 'GeekShop - Регистрация'
        return context


class UserUpdateView(UpdateView):
    model = User
    template_name = 'adminapp/admin-users-update.html'
    form_class = UserAdminProfileForm
    success_url = reverse_lazy('admins:admin_users_read')

    @method_decorator(user_passes_test(lambda u: u.is_superuser, login_url='/'))
    def dispatch(self, request, *args, **kwargs):
        return super(UserUpdateView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(UserUpdateView, self).get_context_data(**kwargs)
        context['title'] = 'GeekShop - Редактирование'
        return context


class UserDeleteView(DeleteView):
    model = User
    template_name = 'adminapp/admin-users-update.html'
    success_url = reverse_lazy('admins:admin_users_read')

    @method_decorator(user_passes_test(lambda u: u.is_superuser, login_url='/'))
    def dispatch(self, request, *args, **kwargs):
        return super(UserDeleteView, self).dispatch(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.is_active = False
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


class ProductListView(ListView):
    model = Product
    template_name = 'adminapp/admin-products-read.html'

    @method_decorator(user_passes_test(lambda u: u.is_superuser, login_url='/'))
    def dispatch(self, request, *args, **kwargs):
        return super(ProductListView, self).dispatch(request, *args, **kwargs)


class ProductCreateView(CreateView):
    model = Product
    template_name = 'adminapp/admin-products-create.html'
    form_class = ProductAdminCreateForm
    success_url = reverse_lazy('admins:admin_products_read')

    @method_decorator(user_passes_test(lambda u: u.is_superuser, login_url='/'))
    def dispatch(self, request, *args, **kwargs):
        return super(ProductCreateView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(ProductCreateView, self).get_context_data(**kwargs)
        context['title'] = 'GeekShop - Добавление продукта'
        return context


class ProductUpdateView(UpdateView):
    model = Product
    template_name = 'adminapp/admin-products-update-delete.html'
    form_class = ProductAdminUpdateForm
    success_url = reverse_lazy('admins:admin_products_read')

    @method_decorator(user_passes_test(lambda u: u.is_superuser, login_url='/'))
    def dispatch(self, request, *args, **kwargs):
        return super(ProductUpdateView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(ProductUpdateView, self).get_context_data(**kwargs)
        context['title'] = 'GeekShop - Редактирование продукта'
        return context


class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'adminapp/admin-products-update-delete.html'
    success_url = reverse_lazy('admins:admin_products_read')

    @method_decorator(user_passes_test(lambda u: u.is_superuser, login_url='/'))
    def dispatch(self, request, *args, **kwargs):
        return super(ProductDeleteView, self).dispatch(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.quantity = 0
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())
