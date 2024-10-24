# Generated by Django 5.1.2 on 2024-10-21 12:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("itr", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="employee",
            name="passport",
            field=models.OneToOneField(
                help_text="Выбери паспорт сотрудника",
                on_delete=django.db.models.deletion.CASCADE,
                related_name="passports",
                to="itr.passportsnilsinn",
                verbose_name="Паспорт",
            ),
        ),
        migrations.AlterField(
            model_name="passportsnilsinn",
            name="employee",
            field=models.OneToOneField(
                help_text="Выбери сотрудника",
                on_delete=django.db.models.deletion.CASCADE,
                to="itr.employee",
                verbose_name="Сотрудник",
            ),
        ),
    ]
