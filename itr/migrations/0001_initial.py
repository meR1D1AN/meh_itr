# Generated by Django 5.1.5 on 2025-01-20 19:38

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(blank=True, help_text='Введите имя компании заказчика', max_length=50, null=True, verbose_name='Заказчик')),
                ('address_customer', models.CharField(blank=True, help_text='Введите адрес объекта, где будет работать сотрудник', max_length=100, null=True, verbose_name='Адрес')),
                ('salary', models.PositiveIntegerField(blank=True, help_text='Введите ЗП сотрудника', null=True, verbose_name='ЗП')),
                ('work_schedule', models.CharField(blank=True, choices=[('2/2', '2 дня через 2 дня'), ('1/3', 'сутки через трое'), ('5/2', '5 дней рабочих 2 дня выходных')], help_text='Выберите график работы сотрудника', max_length=10, null=True, verbose_name='График работы')),
                ('start_work', models.DateField(blank=True, help_text='От этой даты будет зависеть график работы', null=True, verbose_name='Дата начала работы')),
                ('contract', models.FileField(blank=True, help_text='Загрузите договор в формате PDF', null=True, upload_to='contracts/', verbose_name='Договора')),
                ('responsible_person', models.CharField(blank=True, help_text='ФИО ответственного', max_length=100, null=True, verbose_name='Ответственный на объекте')),
                ('contact_phone', models.CharField(blank=True, help_text='Введите номер телефона', max_length=15, null=True, verbose_name='Телефон ответственного')),
                ('contact_email', models.EmailField(blank=True, help_text='Введите email ответственного', max_length=254, null=True, verbose_name='Email ответственного')),
                ('firm', models.CharField(blank=True, choices=[('ООО ГК "ЛифтСервис"', 'ООО ГК "ЛифтСервис"'), ('ООО "ЦентрСервис"', 'ООО "ЦентрСервис"'), ('ООО Холдинг "ЦентрСервис"', 'ООО Холдинг "ЦентрСервис"')], help_text='Выберете исполнителя', null=True, verbose_name='Исполнитель')),
            ],
            options={
                'verbose_name': 'Заказчик',
                'verbose_name_plural': 'Заказчики',
            },
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_name', models.CharField(help_text='Введите фамилию сотрудника', max_length=30, verbose_name='Фамилия')),
                ('first_name', models.CharField(help_text='Введите имя сотрудника', max_length=30, verbose_name='Имя')),
                ('middle_name', models.CharField(blank=True, default='', help_text='Введите отчество сотрудника', max_length=45, null=True, verbose_name='Отчество')),
                ('firm', models.CharField(blank=True, choices=[('ООО ГК "ЛифтСервис"', 'ООО ГК "ЛифтСервис"'), ('ООО "ЦентрСервис"', 'ООО "ЦентрСервис"'), ('ООО Холдинг "ЦентрСервис"', 'ООО Холдинг "ЦентрСервис"')], help_text='Выберете в какой фирме будет работать сотрудник', null=True, verbose_name='Фирма')),
                ('position', models.CharField(choices=[('Лифтёр', 'Лифтёр'), ('Лифтёр проводник', 'Лифтёр проводник'), ('Лифтёр обходчик', 'Лифтёр обходчик'), ('Диспетчер/Оператор', 'Диспетчер/Оператор')], help_text='Выберите должность сотрудника', max_length=30, verbose_name='Должность')),
                ('phone', models.CharField(help_text='Введите телефон сотрудника в формате +79991234567', max_length=13, unique=True, verbose_name='Телефон')),
                ('serial', models.CharField(blank=True, help_text='в формате 1234', max_length=4, null=True, validators=[django.core.validators.RegexValidator('^\\d{4}$', 'Серия паспорта должна состоять из 4 цифр.')], verbose_name='Серия паспорта')),
                ('number', models.CharField(blank=True, help_text='в формате 123456', max_length=6, null=True, validators=[django.core.validators.RegexValidator('^\\d{6}$', 'Номер паспорта должен состоять из 6 цифр.')], verbose_name='Номер паспорта')),
                ('issued_by', models.CharField(blank=True, help_text='Введите кем выдан паспорт', max_length=100, null=True, verbose_name='Кем выдан')),
                ('issued_when', models.DateField(blank=True, help_text='Выберете дату выданы паспорта', null=True, verbose_name='Когда выдан')),
                ('date_of_birth', models.DateField(blank=True, help_text='Выберете дату рождения', null=True, verbose_name='Дата рождения')),
                ('place_of_birth', models.CharField(blank=True, help_text='Введите место рождения', max_length=100, null=True, verbose_name='Место рождения')),
                ('addres_registration', models.CharField(blank=True, help_text='Введите адрес регистрации', max_length=100, null=True, verbose_name='Адрес регистрации')),
                ('date_registration', models.DateField(blank=True, help_text='Выберете дату регистрации', null=True, verbose_name='Дата регистрации')),
                ('snils', models.CharField(blank=True, help_text='Введите СНИЛС в формате 123-456-789 00', max_length=14, null=True, validators=[django.core.validators.RegexValidator('^\\d{3}-\\d{3}-\\d{3} \\d{2}$', 'СНИЛС должен быть в формате 123-456-789 00.')], verbose_name='СНИЛС')),
                ('inn', models.CharField(blank=True, help_text='Введите ИНН в формате 123456789012', max_length=12, null=True, validators=[django.core.validators.RegexValidator('^\\d{12}$', 'ИНН должен состоять из 12 цифр.')], verbose_name='ИНН')),
                ('metro', models.CharField(help_text='Выберите метро', max_length=100, verbose_name='Метро')),
                ('residential_address', models.CharField(help_text='Введите адрес проживания', max_length=100, verbose_name='Адрес проживания')),
                ('education', models.CharField(choices=[('Среднее', 'Среднее'), ('Среднее техническое', 'Среднее техническое'), ('Среднее профессиональное', 'Среднее профессиональное'), ('Высшее', 'Высшее')], help_text='Выбери образование сотрудника', max_length=30, verbose_name='Образование')),
                ('cok', models.FileField(blank=True, help_text='Загрузите ЦОК в формате PDF', null=True, upload_to='cok/', verbose_name='ЦОК')),
                ('attestation', models.FileField(blank=True, help_text='Загрузите аттестацию в формате PDF', null=True, upload_to='attestation/', verbose_name='Аттестация')),
                ('personal_data', models.FileField(blank=True, help_text='Загрузите согласие в формате PDF', null=True, upload_to='personal/', verbose_name='Согласие на обработку персональных данных')),
                ('hire_date', models.DateField(blank=True, help_text='Выберете дату приема на работу', null=True, verbose_name='Дата приема на работу')),
                ('date_of_termination', models.DateField(blank=True, help_text='Выберете дату увольнения', null=True, verbose_name='Дата увольнения')),
                ('termination_reason', models.CharField(blank=True, help_text='Введите причину увольнения', max_length=100, null=True, verbose_name='Причина увольнения')),
            ],
            options={
                'verbose_name': 'Сотрудник',
                'verbose_name_plural': 'Сотрудники',
                'ordering': ['last_name'],
            },
        ),
        migrations.CreateModel(
            name='Vacation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField(blank=True, help_text='Выберите дату начала отпуска', null=True, verbose_name='Дата начала отпуска')),
                ('end_date', models.DateField(blank=True, help_text='Выберите дату окончания отпуска', null=True, verbose_name='Дата окончания отпуска')),
                ('status', models.CharField(blank=True, choices=[('pending', 'На согласовании'), ('approved', 'Согласован'), ('rejected', 'Отклонен')], default='pending', max_length=20, null=True, verbose_name='Статус')),
                ('application_file', models.FileField(blank=True, help_text='Загрузите заявление в формате PDF или фото', null=True, upload_to='vacation_applications/', verbose_name='Заявление на отпуск')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата последнего изменения')),
            ],
            options={
                'verbose_name': 'Отпуск',
                'verbose_name_plural': 'Отпуска',
            },
        ),
        migrations.CreateModel(
            name='WorkDay',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('salary', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, null=True)),
            ],
            options={
                'verbose_name': 'Рабочий день',
                'verbose_name_plural': 'Рабочие дни',
            },
        ),
    ]
