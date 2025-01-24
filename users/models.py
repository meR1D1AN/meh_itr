from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models


NULLABLE = {"null": True, "blank": True}


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("Email обязателен")
        email = self.normalize_email(email)
        user = self.model(
            email=email,
            first_name=extra_fields.get('first_name', ''),
            last_name=extra_fields.get('last_name', ''),
            phone=extra_fields.get('phone'),
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        return self.create_user(email, password, **extra_fields)


class User(AbstractUser):
    username = None
    email = models.EmailField(
        verbose_name="Электронная почта", help_text="Введите email", unique=True
    )
    phone = models.CharField(
        max_length=12,
        verbose_name="Номер телефона",
        help_text="в формате +79991234567",
        unique=True,
    )
    first_name = models.CharField(
        max_length=30, verbose_name="Имя", help_text="Введите имя"
    )
    last_name = models.CharField(
        max_length=30, verbose_name="Фамилия", help_text="Введите фамилию"
    )
    middle_name = models.CharField(
        max_length=30, verbose_name="Отчество", help_text="Введите отчество", **NULLABLE
    )
    is_builder = models.BooleanField(verbose_name="Строительный отдел", default=False)
    is_itr = models.BooleanField(verbose_name="ИТР", default=False)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['first_name', 'last_name', 'phone']

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return (
            f"{self.last_name} {self.first_name[0]}. {self.middle_name[0]}."
        )

    def get_count_employees(self):
        return self.employees.count()
