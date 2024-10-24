# Generated by Django 5.1.2 on 2024-10-21 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("itr", "0006_remove_employee_passport_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="employee",
            name="date_of_termination",
            field=models.DateField(
                blank=True,
                help_text="Выберете дату увольнения",
                null=True,
                verbose_name="Дата увольнения",
            ),
        ),
        migrations.AlterField(
            model_name="employee",
            name="hire_date",
            field=models.DateField(
                blank=True,
                help_text="Выберете дату приема на работу",
                null=True,
                verbose_name="Дата приема на работу",
            ),
        ),
        migrations.AlterField(
            model_name="employee",
            name="termination_reason",
            field=models.CharField(
                blank=True,
                help_text="Выберете причину увольнения",
                max_length=100,
                null=True,
                verbose_name="Причина увольнения",
            ),
        ),
    ]
