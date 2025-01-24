from datetime import date
from django.db import models
from django.core.validators import RegexValidator
from users.models import User

NULLABLE = {"null": True, "blank": True}


class GrafikChoices(models.TextChoices):
    r2_v2 = "2/2", "2 дня через 2 дня"
    s1_v3 = "1/3", "сутки через трое"
    r5_v3 = "5/2", "5 дней рабочих 2 дня выходных"


class FirmChoices(models.TextChoices):
    ooogk = 'ООО ГК "ЛифтСервис"', 'ООО ГК "ЛифтСервис"'
    ooocs = 'ООО "ЦентрСервис"', 'ООО "ЦентрСервис"'
    ooohcs = 'ООО Холдинг "ЦентрСервис"', 'ООО Холдинг "ЦентрСервис"'


class EducationChoices(models.TextChoices):
    sred = "Среднее", "Среднее"
    sred_teh = "Среднее техническое", "Среднее техническое"
    sred_prof = "Среднее профессиональное", "Среднее профессиональное"
    vish = "Высшее", "Высшее"


class PositionChoices(models.TextChoices):
    lifter = "Лифтёр", "Лифтёр"
    lifter_prodovnick = "Лифтёр проводник", "Лифтёр проводник"
    lifter_obhodhick = "Лифтёр обходчик", "Лифтёр обходчик"
    operator = "Диспетчер/Оператор", "Диспетчер/Оператор"


class VacationStatus(models.TextChoices):
    PENDING = "pending", "На согласовании"
    APPROVED = "approved", "Согласован"
    REJECTED = "rejected", "Отклонен"


class Customer(models.Model):
    """
    Модель Заказчика с данными о связанных сотрудниках и объекте.
    """

    customer_name = models.CharField(
        max_length=50,
        verbose_name="Заказчик",
        help_text="Введите имя компании заказчика",
        **NULLABLE,
    )
    address_customer = models.CharField(
        max_length=100,
        verbose_name="Адрес",
        help_text="Введите адрес объекта, где будет работать сотрудник",
        **NULLABLE,
    )
    salary = models.PositiveIntegerField(
        verbose_name="ЗП", help_text="Введите ЗП сотрудника", **NULLABLE
    )
    work_schedule = models.CharField(
        max_length=10,
        choices=GrafikChoices.choices,
        verbose_name="График работы",
        help_text="Выберите график работы сотрудника",
        **NULLABLE,
    )
    # Дата начала работы на объекте
    start_work = models.DateField(
        verbose_name="Дата начала работы",
        help_text="От этой даты будет зависеть график работы",
        **NULLABLE,
    )
    # Дополнительная информация о заказчике
    contract = models.FileField(
        upload_to="contracts/",
        verbose_name="Договора",
        help_text="Загрузите договор в формате PDF",
        **NULLABLE,
    )
    responsible_person = models.CharField(
        max_length=100,
        verbose_name="Ответственный на объекте",
        help_text="ФИО ответственного",
        **NULLABLE,
    )
    contact_phone = models.CharField(
        max_length=15,
        verbose_name="Телефон ответственного",
        help_text="Введите номер телефона",
        **NULLABLE,
    )
    contact_email = models.EmailField(
        verbose_name="Email ответственного",
        help_text="Введите email ответственного",
        **NULLABLE,
    )

    # Связь с сотрудниками
    employee = models.ManyToManyField(
        "Employee",
        verbose_name="Сотрудник",
        help_text="Выберите сотрудника",
        related_name="customers",
        blank=True,
    )
    # Создал заказчика ИТР
    created_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        verbose_name="Создано пользователем",
        related_name="customers",
        **NULLABLE,
    )
    # Исполнитель
    firm = models.CharField(
        choices=FirmChoices.choices,
        verbose_name="Исполнитель",
        help_text="Выберете исполнителя",
        **NULLABLE,
    )
    # Исполнитель
    firm = models.CharField(
        choices=FirmChoices.choices,
        verbose_name="Исполнитель",
        help_text="Выберете исполнителя",
        **NULLABLE,
    )

    def __str__(self):
        return f"{self.customer_name} ({self.address_customer})"

    class Meta:
        verbose_name = "Заказчик"
        verbose_name_plural = "Заказчики"


class Employee(models.Model):
    """
    Модель Сотрудника с подробной информацией о его данных и работе.
    """

    # ФИО сотрудника
    last_name = models.CharField(
        max_length=30, verbose_name="Фамилия", help_text="Введите фамилию сотрудника"
    )
    first_name = models.CharField(
        max_length=30, verbose_name="Имя", help_text="Введите имя сотрудника"
    )
    middle_name = models.CharField(
        max_length=45,
        verbose_name="Отчество",
        help_text="Введите отчество сотрудника",
        default="",
        **NULLABLE,
    )
    # К какой фирме относится сотрудник, фирма заказчика, адрес объекта где будет работать, должность
    firm = models.CharField(
        choices=FirmChoices.choices,
        verbose_name="Фирма",
        help_text="Выберете в какой фирме будет работать сотрудник",
        **NULLABLE,
    )
    customer = models.ManyToManyField(
        Customer,
        verbose_name="Заказчик",
        help_text="Выберите заказчика",
        related_name="employees",
        blank=True,
    )
    position = models.CharField(
        max_length=30,
        choices=PositionChoices.choices,
        verbose_name="Должность",
        help_text="Выберите должность сотрудника",
    )
    # Номер телефона сотрудника
    phone = models.CharField(
        max_length=13,
        verbose_name="Телефон",
        help_text="Введите телефон сотрудника в формате +79991234567",
        unique=True,
    )
    # Паспорт и все остальные данные
    serial = models.CharField(
        max_length=4,
        verbose_name="Серия паспорта",
        help_text="в формате 1234",
        validators=[
            RegexValidator(r"^\d{4}$", "Серия паспорта должна состоять из 4 цифр.")
        ],
        **NULLABLE,
    )
    number = models.CharField(
        max_length=6,
        verbose_name="Номер паспорта",
        help_text="в формате 123456",
        validators=[
            RegexValidator(r"^\d{6}$", "Номер паспорта должен состоять из 6 цифр.")
        ],
        **NULLABLE,
    )
    issued_by = models.CharField(
        max_length=100,
        verbose_name="Кем выдан",
        help_text="Введите кем выдан паспорт",
        **NULLABLE,
    )
    issued_when = models.DateField(
        verbose_name="Когда выдан",
        help_text="Выберете дату выданы паспорта",
        **NULLABLE,
    )
    date_of_birth = models.DateField(
        verbose_name="Дата рождения", help_text="Выберете дату рождения", **NULLABLE
    )
    place_of_birth = models.CharField(
        max_length=100,
        verbose_name="Место рождения",
        help_text="Введите место рождения",
        **NULLABLE,
    )
    addres_registration = models.CharField(
        max_length=100,
        verbose_name="Адрес регистрации",
        help_text="Введите адрес регистрации",
        **NULLABLE,
    )
    date_registration = models.DateField(
        verbose_name="Дата регистрации",
        help_text="Выберете дату регистрации",
        **NULLABLE,
    )
    # СНИЛС
    snils = models.CharField(
        max_length=14,
        verbose_name="СНИЛС",
        help_text="Введите СНИЛС в формате 123-456-789 00",
        validators=[
            RegexValidator(
                r"^\d{3}-\d{3}-\d{3} \d{2}$",
                "СНИЛС должен быть в формате 123-456-789 00.",
            )
        ],
        **NULLABLE,
    )
    # ИНН
    inn = models.CharField(
        max_length=12,
        verbose_name="ИНН",
        help_text="Введите ИНН в формате 123456789012",
        validators=[RegexValidator(r"^\d{12}$", "ИНН должен состоять из 12 цифр.")],
        **NULLABLE,
    )

    # Адрес проживания сотрудника
    metro = models.CharField(
        max_length=100, verbose_name="Метро", help_text="Выберите метро"
    )
    residential_address = models.CharField(
        max_length=100,
        verbose_name="Адрес проживания",
        help_text="Введите адрес проживания",
    )
    # Образование
    education = models.CharField(
        max_length=30,
        choices=EducationChoices.choices,
        verbose_name="Образование",
        help_text="Выбери образование сотрудника",
    )
    # Цок сотрудника нужно загружать pdf файл
    cok = models.FileField(
        upload_to="cok/",
        verbose_name="ЦОК",
        help_text="Загрузите ЦОК в формате PDF",
        **NULLABLE,
    )
    # Аттестацию сотрудника нужно загружать pdf файл
    attestation = models.FileField(
        upload_to="attestation/",
        verbose_name="Аттестация",
        help_text="Загрузите аттестацию в формате PDF",
        **NULLABLE,
    )
    # Согласие на обработку персональных данных
    personal_data = models.FileField(
        upload_to="personal/",
        verbose_name="Согласие на обработку персональных данных",
        help_text="Загрузите согласие в формате PDF",
        **NULLABLE,
    )
    # Дата приёма на работу
    hire_date = models.DateField(
        verbose_name="Дата приема на работу",
        help_text="Выберете дату приема на работу",
        **NULLABLE,
    )
    # Дата увольнения
    date_of_termination = models.DateField(
        verbose_name="Дата увольнения", help_text="Выберете дату увольнения", **NULLABLE
    )
    # Причина увольнения
    termination_reason = models.CharField(
        max_length=100,
        verbose_name="Причина увольнения",
        help_text="Введите причину увольнения",
        **NULLABLE,
    )
    # Создал сотрудника ИТР
    created_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        verbose_name="Создано пользователем",
        related_name="employees",
        **NULLABLE,
    )

    def __str__(self):
        if self.middle_name:
            return f"{self.last_name} {self.first_name[0]}. {self.middle_name[0]}."
        else:
            return f"{self.last_name} {self.first_name[0]}."

    def get_age(self):
        today = date.today()
        age = (
            today.year
            - self.date_of_birth.year
            - (
                (today.month, today.day)
                < (self.date_of_birth.month, self.date_of_birth.day)
            )
        )
        return age

    class Meta:
        verbose_name = "Сотрудник"
        verbose_name_plural = "Сотрудники"
        ordering = ["last_name"]


class WorkDay(models.Model):
    employee = models.ForeignKey(
        Employee, on_delete=models.CASCADE, related_name="workdays"
    )
    date = models.DateField()
    salary = models.DecimalField(max_digits=10, decimal_places=2, default=0, **NULLABLE)

    class Meta:
        verbose_name = "Рабочий день"
        verbose_name_plural = "Рабочие дни"

    def __str__(self):
        return f"{self.employee} - {self.salary}"


class Vacation(models.Model):
    employee = models.ForeignKey(
        Employee,
        on_delete=models.CASCADE,
        related_name="vacations",
        verbose_name="Сотрудник",
        **NULLABLE,
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="user_vacations",
        verbose_name="Пользователь",
        **NULLABLE,
    )
    start_date = models.DateField(
        verbose_name="Дата начала отпуска",
        help_text="Выберите дату начала отпуска",
        **NULLABLE,
    )
    end_date = models.DateField(
        verbose_name="Дата окончания отпуска",
        help_text="Выберите дату окончания отпуска",
        **NULLABLE,
    )
    status = models.CharField(
        max_length=20,
        choices=VacationStatus.choices,
        default=VacationStatus.PENDING,
        verbose_name="Статус",
        **NULLABLE,
    )
    application_file = models.FileField(
        upload_to="vacation_applications/",
        verbose_name="Заявление на отпуск",
        help_text="Загрузите заявление в формате PDF или фото",
        **NULLABLE,
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name="Дата последнего изменения"
    )
    created_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        verbose_name="Создано пользователем",
        **NULLABLE,
    )

    class Meta:
        verbose_name = "Отпуск"
        verbose_name_plural = "Отпуска"

    def __str__(self):
        if self.user:
            return f"Отпуск пользователя {self.user.last_name} {self.user.first_name[0]}. : {self.start_date} - {self.end_date}"
        elif self.employee:
            return f"Отпуск сотрудника {self.employee}: {self.start_date} - {self.end_date}"
        return f"Отпуск: {self.start_date} - {self.end_date}"

    @property
    def vacation_days(self):
        return (self.end_date - self.start_date).days + 1
