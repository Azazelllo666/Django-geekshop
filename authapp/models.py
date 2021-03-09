from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.timezone import now

from datetime import timedelta


class User(AbstractUser):
    avatar = models.ImageField(upload_to='users_avatar', blank=True)
    age = models.PositiveSmallIntegerField(blank=True, null=True, default=18)
    activation_key = models.CharField(verbose_name='Ключ подтверждения', max_length=128, blank=True)
    activation_key_expires = models.DateTimeField(
        verbose_name='Актуальность ключа', default=(now() + timedelta(hours=48))
    )

    def is_activation_key_expired(self):
        if now() <= self.activation_key_expires:
            return False
        else:
            return True
