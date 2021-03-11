from django.db import migrations, transaction


def forwards_func(apps, schema_editor):
    try:
        User = apps.get_model("authapp", "User")
        UserProfile = apps.get_model("authapp", "UserProfile")

        with transaction.atomic():
            qs = User.objects.all()
            for item in qs:
                UserProfile.objects.create(user=item)
    except Exception as exp:
        print(f"Cann't create user profile: {exp}")


def reverse_func(apps, schema_editor):
    try:
        UserProfile = apps.get_model("authapp", "UserProfile")

        with transaction.atomic():
            UserProfile.objects.all().delete()
    except Exception as exp:
        print(f"Cann't delete users profiles: {exp}")


class Migration(migrations.Migration):
    dependencies = [
        ("authapp", "0004_user_profile"),
    ]

    operations = [migrations.RunPython(forwards_func, reverse_func)]
