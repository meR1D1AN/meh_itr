from django.core.management import BaseCommand
from django.contrib.auth.models import User


class Command(BaseCommand):
    help = "Создание учётки админа"

    def handle(self, *args, **options):
        user = User.objects.create(
            username="admin",
            first_name="Admin",
            last_name="Adminov",
            email="admin@admin.ru",
            is_superuser=True,
            is_staff=True,
            is_active=True,
        )
        user.set_password("qwe123")
        user.save()
