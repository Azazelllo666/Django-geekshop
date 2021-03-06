# Generated by Django 2.2.17 on 2021-03-09 17:56

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0002_user_model_extend'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='activation_key_expires',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 11, 17, 56, 14, 54530, tzinfo=utc), verbose_name='Актуальность ключа'),
        ),
        migrations.AlterField(
            model_name='user',
            name='age',
            field=models.PositiveSmallIntegerField(blank=True, default=18, null=True),
        ),
    ]
