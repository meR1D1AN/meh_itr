# Generated by Django 5.1.2 on 2024-10-21 11:49

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Employee",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "first_name",
                    models.CharField(
                        help_text="Введите имя сотрудника",
                        max_length=30,
                        verbose_name="Имя",
                    ),
                ),
                (
                    "last_name",
                    models.CharField(
                        help_text="Введите фамилию сотрудника",
                        max_length=30,
                        verbose_name="Фамилия",
                    ),
                ),
                (
                    "middle_name",
                    models.CharField(
                        help_text="Введите отчество сотрудника",
                        max_length=30,
                        verbose_name="Отчество",
                    ),
                ),
                (
                    "position",
                    models.CharField(
                        choices=[
                            ("Лифтёр", "Лифтёр"),
                            ("Лифтёр проводник", "Лифтёр проводник"),
                            ("Лифтёр обходчик", "Лифтёр обходчик"),
                            ("Диспетчер/Оператор", "Диспетчер/Оператор"),
                        ],
                        help_text="Выберите должность сотрудника",
                        max_length=30,
                        verbose_name="Должность",
                    ),
                ),
                (
                    "phone",
                    models.CharField(
                        help_text="Введите телефон сотрудника в формате +79991234567",
                        max_length=13,
                        verbose_name="Телефон",
                    ),
                ),
                (
                    "metro",
                    models.CharField(
                        help_text="Выберите метро", max_length=100, verbose_name="Метро"
                    ),
                ),
                (
                    "residential_address",
                    models.CharField(
                        help_text="Введите адрес проживания",
                        max_length=100,
                        verbose_name="Адрес проживания",
                    ),
                ),
                (
                    "education",
                    models.CharField(
                        choices=[
                            ("Среднее", "Среднее"),
                            ("Среднее техническое", "Среднее техническое"),
                            ("Среднее профессиональное", "Среднее профессиональное"),
                            ("Высшее", "Высшее"),
                        ],
                        help_text="Выбери образование сотрудника",
                        max_length=30,
                        verbose_name="Образование",
                    ),
                ),
                (
                    "cok",
                    models.FileField(
                        blank=True,
                        help_text="Загрузите ЦОК в формате PDF",
                        null=True,
                        upload_to="cok/",
                        verbose_name="ЦОК",
                    ),
                ),
                (
                    "attestation",
                    models.FileField(
                        blank=True,
                        help_text="Загрузите аттестацию в формате PDF",
                        null=True,
                        upload_to="attestation/",
                        verbose_name="Аттестация",
                    ),
                ),
                (
                    "hire_date",
                    models.DateField(
                        help_text="Выберете дату приема на работу",
                        verbose_name="Дата приема на работу",
                    ),
                ),
                (
                    "date_of_termination",
                    models.DateField(
                        blank=True,
                        help_text="Выберете дату увольнения",
                        verbose_name="Дата увольнения",
                    ),
                ),
                (
                    "termination_reason",
                    models.CharField(
                        blank=True,
                        help_text="Выберете причину увольнения",
                        max_length=100,
                        verbose_name="Причина увольнения",
                    ),
                ),
            ],
            options={
                "verbose_name": "Сотрудник",
                "verbose_name_plural": "Сотрудники",
            },
        ),
        migrations.CreateModel(
            name="PassportSnilsInn",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "serial",
                    models.CharField(
                        help_text="Введите серию паспорта в формате 1234",
                        max_length=4,
                        validators=[
                            django.core.validators.RegexValidator(
                                "^\\d{4}$", "Серия паспорта должна состоять из 4 цифр."
                            )
                        ],
                        verbose_name="Серия паспорта",
                    ),
                ),
                (
                    "number",
                    models.CharField(
                        help_text="Введите номер паспорта в формате 123456",
                        max_length=6,
                        validators=[
                            django.core.validators.RegexValidator(
                                "^\\d{6}$", "Номер паспорта должен состоять из 6 цифр."
                            )
                        ],
                        verbose_name="Номер паспорта",
                    ),
                ),
                (
                    "issued_by",
                    models.CharField(
                        help_text="Введите кем выдан паспорт",
                        max_length=100,
                        verbose_name="Кем выдан",
                    ),
                ),
                (
                    "issued_when",
                    models.DateField(
                        help_text="Выберете дату выданы паспорта",
                        verbose_name="Когда выдан",
                    ),
                ),
                (
                    "date_of_birth",
                    models.DateField(
                        help_text="Выберете дату рождения", verbose_name="Дата рождения"
                    ),
                ),
                (
                    "place_of_birth",
                    models.CharField(
                        help_text="Введите место рождения",
                        max_length=100,
                        verbose_name="Место рождения",
                    ),
                ),
                (
                    "addres_registration",
                    models.CharField(
                        help_text="Введите адрес регистрации",
                        max_length=100,
                        verbose_name="Адрес регистрации",
                    ),
                ),
                (
                    "date_registration",
                    models.DateField(
                        help_text="Выберете дату регистрации",
                        verbose_name="Дата регистрации",
                    ),
                ),
                (
                    "snils",
                    models.CharField(
                        help_text="Введите СНИЛС в формате 123-456-789 00",
                        max_length=14,
                        validators=[
                            django.core.validators.RegexValidator(
                                "^\\d{3}-\\d{3}-\\d{3} \\d{2}$",
                                "СНИЛС должен быть в формате 123-456-789 00.",
                            )
                        ],
                        verbose_name="СНИЛС",
                    ),
                ),
                (
                    "inn",
                    models.CharField(
                        help_text="Введите ИНН в формате 123456789012",
                        max_length=12,
                        validators=[
                            django.core.validators.RegexValidator(
                                "^\\d{12}$", "ИНН должен состоять из 12 цифр."
                            )
                        ],
                        verbose_name="ИНН",
                    ),
                ),
                (
                    "employee",
                    models.ForeignKey(
                        help_text="Выбери сотрудника",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="itr.employee",
                        verbose_name="Сотрудник",
                    ),
                ),
            ],
            options={
                "verbose_name": "Паспорт",
                "verbose_name_plural": "Паспорта",
            },
        ),
        migrations.AddField(
            model_name="employee",
            name="passport",
            field=models.ForeignKey(
                help_text="Выбери паспорт сотрудника",
                on_delete=django.db.models.deletion.CASCADE,
                related_name="passports",
                to="itr.passportsnilsinn",
                verbose_name="Паспорт",
            ),
        ),
    ]