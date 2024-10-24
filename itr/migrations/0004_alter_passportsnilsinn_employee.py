# Generated by Django 5.1.2 on 2024-10-21 12:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("itr", "0003_alter_passportsnilsinn_employee"),
    ]

    operations = [
        migrations.AlterField(
            model_name="passportsnilsinn",
            name="employee",
            field=models.OneToOneField(
                blank=True,
                help_text="Выбери сотрудника",
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="itr.employee",
                verbose_name="Сотрудник",
            ),
        ),
    ]
