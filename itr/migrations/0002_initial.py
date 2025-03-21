# Generated by Django 5.1.5 on 2025-01-20 19:38

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('itr', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='customers', to=settings.AUTH_USER_MODEL, verbose_name='Создано пользователем'),
        ),
        migrations.AddField(
            model_name='employee',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='employees', to=settings.AUTH_USER_MODEL, verbose_name='Создано пользователем'),
        ),
        migrations.AddField(
            model_name='employee',
            name='customer',
            field=models.ManyToManyField(blank=True, help_text='Выберите заказчика', related_name='employees', to='itr.customer', verbose_name='Заказчик'),
        ),
        migrations.AddField(
            model_name='customer',
            name='employee',
            field=models.ManyToManyField(blank=True, help_text='Выберите сотрудника', related_name='customers', to='itr.employee', verbose_name='Сотрудник'),
        ),
        migrations.AddField(
            model_name='vacation',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Создано пользователем'),
        ),
        migrations.AddField(
            model_name='vacation',
            name='employee',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='vacations', to='itr.employee', verbose_name='Сотрудник'),
        ),
        migrations.AddField(
            model_name='vacation',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_vacations', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
        migrations.AddField(
            model_name='workday',
            name='employee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='workdays', to='itr.employee'),
        ),
    ]
