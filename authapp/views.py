from django.shortcuts import render, HttpResponseRedirect
from django.contrib import auth, messages
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.core.mail import send_mail

from authapp.forms import UserLoginForm, UserRegisterForm, UserProfileForm
from authapp.models import User
from basket.models import Basket


def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user and user.is_active:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('index'))
    else:
        form = UserLoginForm()
    context = {
        'title': 'GeekShop - Авторизация',
        'form': form,
    }
    return render(request, 'authapp/login.html', context)


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, 'Вы успешно зарегистрировались!')
            if send_verify_mail(user):
                print('Сообщение для подтверждения регистрации отправлено')
                return HttpResponseRedirect(reverse('auth:login'))
            print('Ошибка отправки сообщения для подтверждения регистрации')
            return HttpResponseRedirect(reverse('auth:login'))
    else:
        form = UserRegisterForm()
    context = {
        'title': 'GeekShop - Регистрация',
        'form': form,
    }
    return render(request, 'authapp/register.html', context)


def send_verify_mail(user):
    verify_link = reverse("auth:verify", args=[user.email, user.activation_key])

    title = f"Подтверждение учетной записи {user.username}"
    message = f"Для подтверждения учетной записи {user.username} \
    на портале {settings.DOMAIN_NAME} перейдите по ссылке: \
    \n{settings.DOMAIN_NAME}{verify_link}"

    print(f"from: {settings.EMAIL_HOST_USER}, to: {user.email}")
    return send_mail(title, message, settings.EMAIL_HOST_USER, [user.email], fail_silently=False, )


def verify(request, email, activation_key):
    try:
        user = User.objects.get(email=email)
        if user.activation_key == activation_key and not user.is_activation_key_expired():
            print(f"user {user} is activated")
            user.is_active = True
            user.save()
            auth.login(request, user)

            return render(request, "authapp/verification.html")
        print(f"error activation user: {user}")
        return render(request, "authapp/verification.html")

    except Exception as e:
        print(f"error activation user : {e.args}")
    return HttpResponseRedirect(reverse('index'))


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('index'))


@login_required
def profile(request):
    if request.method == 'POST':
        form = UserProfileForm(data=request.POST, files=request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('auth:profile'))
    else:
        form = UserProfileForm(instance=request.user)

    context = {
        'title': 'GeekShop - Профиль',
        'form': form,
        'baskets': Basket.objects.filter(user=request.user),
    }
    return render(request, 'authapp/profile.html', context)
