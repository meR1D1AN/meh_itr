from datetime import date

from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import User

NULLABLE = {'null': True, 'blank': True}


class Employee(models.Model):
    sred = "Среднее"
    sred_teh = "Среднее техническое"
    sred_prof = "Среднее профессиональное"
    vish = "Высшее"

    education_choices = [
        (sred, "Среднее"),
        (sred_teh, "Среднее техническое"),
        (sred_prof, "Среднее профессиональное"),
        (vish, "Высшее"),
    ]

    lifter = "Лифтёр"
    lifter_prodovnick = "Лифтёр проводник"
    lifter_obhodhick = "Лифтёр обходчик"
    operator = "Диспетчер/Оператор"

    position_choices = [
        (lifter, "Лифтёр"),
        (lifter_prodovnick, "Лифтёр проводник"),
        (lifter_obhodhick, "Лифтёр обходчик"),
        (operator, "Диспетчер/Оператор"),
    ]
    # ФИО сотрудника
    last_name = models.CharField(max_length=30, verbose_name="Фамилия", help_text="Введите фамилию сотрудника")
    first_name = models.CharField(max_length=30, verbose_name="Имя", help_text="Введите имя сотрудника")
    middle_name = models.CharField(max_length=30, verbose_name="Отчество", help_text="Введите отчество сотрудника")
    # Должность
    position = models.CharField(max_length=30, choices=position_choices, verbose_name="Должность",
                                help_text="Выберите должность сотрудника")
    # Номер телефона сотрудника
    phone = models.CharField(max_length=13, verbose_name="Телефон",
                             help_text="Введите телефон сотрудника в формате +79991234567", unique=True)
    # Паспорт и все остальные данные
    serial = models.CharField(max_length=4, verbose_name="Серия паспорта",
                              help_text="Введите серию паспорта в формате 1234",
                              validators=[RegexValidator(r'^\d{4}$', 'Серия паспорта должна состоять из 4 цифр.')],
                              **NULLABLE)
    number = models.CharField(max_length=6, verbose_name="Номер паспорта",
                              help_text="Введите номер паспорта в формате 123456",
                              validators=[RegexValidator(r'^\d{6}$', 'Номер паспорта должен состоять из 6 цифр.')],
                              **NULLABLE)
    issued_by = models.CharField(max_length=100, verbose_name="Кем выдан",
                                 help_text="Введите кем выдан паспорт", **NULLABLE)
    issued_when = models.DateField(verbose_name="Когда выдан", help_text="Выберете дату выданы паспорта", **NULLABLE)
    date_of_birth = models.DateField(verbose_name="Дата рождения", help_text="Выберете дату рождения", **NULLABLE)
    place_of_birth = models.CharField(max_length=100, verbose_name="Место рождения", help_text="Введите место рождения",
                                      **NULLABLE)
    addres_registration = models.CharField(max_length=100, verbose_name="Адрес регистрации",
                                           help_text="Введите адрес регистрации", **NULLABLE)
    date_registration = models.DateField(verbose_name="Дата регистрации", help_text="Выберете дату регистрации",
                                         **NULLABLE)
    # СНИЛС
    snils = models.CharField(max_length=14, verbose_name="СНИЛС",
                             help_text="Введите СНИЛС в формате 123-456-789 00",
                             validators=[RegexValidator(r'^\d{3}-\d{3}-\d{3} \d{2}$',
                                                        'СНИЛС должен быть в формате 123-456-789 00.')], **NULLABLE)
    # ИНН
    inn = models.CharField(max_length=12, verbose_name="ИНН",
                           help_text="Введите ИНН в формате 123456789012",
                           validators=[RegexValidator(r'^\d{12}$', 'ИНН должен состоять из 12 цифр.')], **NULLABLE)

    # Адрес проживания сотрудника
    metro = models.CharField(max_length=100, verbose_name="Метро", help_text="Выберите метро")
    residential_address = models.CharField(max_length=100, verbose_name="Адрес проживания",
                                           help_text="Введите адрес проживания")
    # Образование
    education = models.CharField(max_length=30, choices=education_choices, verbose_name="Образование",
                                 help_text="Выбери образование сотрудника")
    # Цок сотрудника нужно загружать pdf файл
    cok = models.FileField(upload_to='cok/', verbose_name="ЦОК", help_text="Загрузите ЦОК в формате PDF", **NULLABLE)
    # Аттестацию сотрудника нужно загружать pdf файл
    attestation = models.FileField(upload_to='attestation/', verbose_name="Аттестация",
                                   help_text="Загрузите аттестацию в формате PDF", **NULLABLE)
    # Дата приёма на работу
    hire_date = models.DateField(verbose_name="Дата приема на работу", help_text="Выберете дату приема на работу",
                                 **NULLABLE)
    # Дата увольнения
    date_of_termination = models.DateField(verbose_name="Дата увольнения", help_text="Выберете дату увольнения",
                                           **NULLABLE)
    # Причина увольнения
    termination_reason = models.CharField(max_length=100, verbose_name="Причина увольнения",
                                          help_text="Выберете причину увольнения", **NULLABLE)
    # Создал сотрудника ИТР
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, verbose_name="Создано пользователем", **NULLABLE)

    def __str__(self):
        return f"{self.last_name} {self.first_name[0]}. {self.middle_name[0]}."

    def get_birth_date_with_age(self):
        today = date.today()
        age = today.year - self.date_of_birth.year - (
                    (today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day))
        return f" (Возраст {age})"

    class Meta:
        verbose_name = "Сотрудник"
        verbose_name_plural = "Сотрудники"


class Object(models.Model):
    ooogk = 'ООО ГК "ЛифтСервис"'
    ooocs = 'ООО "ЦентрСервис"'
    ooohcs = 'ООО Холдинг "ЦентрСервис"'
    ooo_firm = [
        (ooogk, 'ООО ГК "ЛифтСервис"'),
        (ooocs, 'ООО "ЦентрСервис"'),
        (ooohcs, 'ООО Холдинг "ЦентрСервис"'),
    ]

    firm = models.CharField(max_length=30, choices=ooo_firm, verbose_name="Фирма", help_text="Выберите фирму")
    address = models.CharField(max_length=100, verbose_name="Адрес", help_text="Введите адрес")
