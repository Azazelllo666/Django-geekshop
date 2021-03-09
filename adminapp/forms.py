from django import forms
from django.forms import ModelForm

from authapp.forms import UserRegisterForm, UserProfileForm
from authapp.models import User
from mainapp.models import Product, ProductCategory


class UserAdminRegisterForm(UserRegisterForm):
    avatar = forms.ImageField(widget=forms.FileInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2', 'avatar')

    def __init__(self, *args, **kwargs):
        super(UserAdminRegisterForm, self).__init__(*args, **kwargs)
        self.fields['avatar'].widget.attrs['class'] = 'custom-file-input'


class UserAdminProfileForm(UserProfileForm):
    def __init__(self, *args, **kwargs):
        super(UserAdminProfileForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['readonly'] = False
        self.fields['email'].widget.attrs['readonly'] = False


class ProductAdminCreateForm(ModelForm):
    price = forms.DecimalField(label='Цена', decimal_places=2)
    quantity = forms.DecimalField(label='Количество')
    image = forms.ImageField(widget=forms.FileInput())

    class Meta:
        model = Product
        fields = ('name', 'image', 'description', 'short_description', 'price', 'quantity', 'category')

    def __init__(self, *args, **kwargs):
        super(ProductAdminCreateForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['placeholder'] = 'Введите название продукта'
        self.fields['image'].widget.attrs['placeholder'] = 'Добавьте картинку'
        self.fields['description'].widget.attrs['placeholder'] = 'Введите Описание продукта'
        self.fields['short_description'].widget.attrs['placeholder'] = 'Введите короткое описание продукта'
        self.fields['price'].widget.attrs['placeholder'] = 'Введите стоимость'
        self.fields['quantity'].widget.attrs['placeholder'] = 'Введите количество продукта'
        self.fields['category'].widget.attrs['placeholder'] = 'Введите категорию'

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control py-4'
        self.fields['image'].widget.attrs['class'] = 'custom-file-input'
        self.fields['category'].widget.attrs['class'] = 'form-control'


class ProductAdminUpdateForm(ModelForm):
    image = forms.ImageField(widget=forms.FileInput())
    price = forms.DecimalField(label='Цена', decimal_places=2)
    quantity = forms.DecimalField(label='Количество')

    class Meta:
        model = Product
        fields = ('name', 'image', 'description', 'short_description', 'price', 'quantity', 'category')

    def __init__(self, *args, **kwargs):
        super(ProductAdminUpdateForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control py-4'
        self.fields['image'].widget.attrs['class'] = 'custom-file-input'
        self.fields['category'].widget.attrs['class'] = 'form-control'


class ProductCategoryAdminCreateForm(ModelForm):
    class Meta:
        model = ProductCategory
        fields = ('name', 'description')

    def __init__(self, *args, **kwargs):
        super(ProductCategoryAdminCreateForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['placeholder'] = 'Введите название категории'
        self.fields['description'].widget.attrs['placeholder'] = 'Введите описание категории'

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control py-4'


class ProductCategoryAdminUpdateForm(ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'description')

    def __init__(self, *args, **kwargs):
        super(ProductCategoryAdminUpdateForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control py-4'