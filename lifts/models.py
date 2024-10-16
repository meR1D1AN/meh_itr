from django.db import models


class Building(models.Model):
    """
    Класс для записи адресов зданий с лифтами
    """

    D36 = "D36"
    D36STR9 = "D36STR9"
    D36STR10 = "D36STR10"
    D36STR11 = "D36STR11"
    D36STR28 = "D36STR28"
    D36STR41 = "D36STR41"
    MSTK = "MSTK"

    BUILDS = [
        (D36, "д. 36"),
        (D36STR9, "д. 36 стр. 9"),
        (D36STR10, "д. 36 стр. 10"),
        (D36STR11, "д. 36 стр. 11"),
        (D36STR28, "д. 36 стр. 28"),
        (D36STR41, "д. 36 стр. 41"),
        (MSTK, "МСТК"),
    ]

    address = models.CharField(
        choices=BUILDS,
        max_length=14,
        default=D36,
        verbose_name="Адрес",
        help_text="Выбери адрес",
    )
    elevators = models.ManyToManyField(
        "Elevator", verbose_name="Лифты", related_name="buildings", blank=True
    )

    def __str__(self):
        return self.get_address_display()

    class Meta:
        verbose_name = "Здание"
        verbose_name_plural = "Здания"


class Elevator(models.Model):
    """
    Класс для лифтов
    """

    P1 = "P1"
    P2 = "P2"
    P3 = "P3"
    P4 = "P4"
    P5 = "P5"
    P6 = "P6"
    P7 = "P7"
    P8 = "P8"
    P9 = "P9"
    P12 = "P12"
    P13 = "P13"
    P14 = "P14"
    P15 = "P15"
    P16 = "P16"
    P17 = "P17"
    P18 = "P18"
    P19 = "P19"
    SV1 = "SV1"
    SV2 = "SV2"
    SV3 = "SV3"
    SV4 = "SV4"
    SV5 = "SV5"
    SV6 = "SV6"
    SV7 = "SV7"
    SV8 = "SV8"
    L_A9 = "L_A9"
    L_B9 = "L_B9"
    L_C9 = "L_C9"
    L_D9 = "L_D9"
    L_GENERAL9 = "L_GENERAL9"
    L_KUHONIE9 = "L_KOHONIE9"
    L_GRUZ19 = "L_GRUZ19"
    L_GRUZ29 = "L_GRUZ29"
    L_PARK9 = "L_PARK9"
    L_A10 = "L_A10"
    L_B10 = "L_B10"
    L_C10 = "L_C10"
    L_GRUZ10 = "L_GRUZ10"
    L_PARK10 = "L_PARK10"
    L_A11 = "L_A11"
    L_B11 = "L_B11"
    L_C11 = "L_C11"
    L_GRUZ11 = "L_GRUZ11"
    L_PARK11 = "L_PARK11"
    L_KUHONIE11 = "L_KUHONIE11"
    OTIS_MUSEI = "OTIS_MUSEI"
    STEKLYANIE_MUSEI = "STEKLYANIE_MUSEI"
    L1 = "L1"
    L2 = "L2"
    L3 = "L3"
    L4 = "L4"
    L5 = "L5"
    L6 = "L6"
    L7 = "L7"
    L8 = "L8"
    L9 = "L9"
    L10 = "L10"
    L11 = "L11"
    L12 = "L12"
    L13 = "L13"
    L14 = "L14"
    L15 = "L15"
    MSTK_L1 = "MSTK_L1"

    ELEVATORS = [
        (P1, "Лифт Р1 - 42422309"),
        (P2, "Лифт Р2 - 42422311"),
        (P3, "Лифт Р3 - 42422310"),
        (P4, "Лифт Р4 - 42422312"),
        (P5, "Лифт Р5 - 42422313"),
        (P6, "Лифт Р6 - 42422314"),
        (P7, "Лифт Р7 - 42422315"),
        (P8, "Лифт Р8 - 42422316"),
        (P9, "Лифт Р9 - 42422317"),
        (P12, "Лифт Р12 - 42422320"),
        (P13, "Лифт Р13 - 42422321"),
        (P14, "Лифт Р14 - 42422322"),
        (P15, "Лифт Р15 - 42422323"),
        (P16, "Лифт Р16 - 42422324"),
        (P17, "Лифт Р17 - 42422325"),
        (P18, "Лифт Р18 - 42422326"),
        (P19, "Лифт Р19 - 42422327"),
        (SV1, "Лифт SV-1 - 42422329"),
        (SV2, "Лифт SV-2 - 42422328"),
        (SV3, "Лифт SV-3 - 42422330"),
        (SV4, "Лифт SV-4 - 42422331"),
        (SV5, "Лифт SV-5 - 42422332"),
        (SV6, "Лифт SV-6 - 42422333"),
        (SV7, "Лифт SV-7 - 42422334"),
        (SV8, "Лифт SV-8 - 42422335"),
        (L_A9, "Лифт №1 - E2NI5471"),
        (L_B9, "Лифт №2 - E2NI5472"),
        (L_C9, "Лифт №3 - E2NI5473"),
        (L_D9, "Лифт №4 - E2NI5474"),
        (L_GENERAL9, "Лифт Генеральский - E2NI5475"),
        (L_KUHONIE9, "Лифт Кухонный - E2NI5476"),
        (L_GRUZ19, "Лифт Грузовой левый - E2NI5477"),
        (L_GRUZ29, "Лифт Грузовой правый - E2NO0160"),
        (L_PARK9, "Лифт Парковочный - E2NI5478"),
        (L_A10, "Лифт А10 - E2NI5480"),
        (L_B10, "Лифт Б10 - E2NI5479"),
        (L_C10, "Лифт С10 - E2NI5481"),
        (L_GRUZ10, "Лифт Грузовой - E2NI5482"),
        (L_PARK10, "Лифт Парковочный - E2NI5485"),
        (L_A11, "Лифт А11 - E2NI5486"),
        (L_B11, "Лифт Б11 - E2NI5487"),
        (L_C11, "Лифт С11 - E2NI5488"),
        (L_GRUZ11, "Лифт Грузовой - E2NI5489"),
        (L_PARK11, "Лифт Парковочный - E2NI5490"),
        (L_KUHONIE11, "Лифт Кухонный - E2NI5492"),
        (OTIS_MUSEI, "Лифт Отис - E2NO3091"),
        (STEKLYANIE_MUSEI, "Лифт Стеклянный - 311456"),
        (L1, "Лифт L1 - 43686519"),
        (L2, "Лифт L2 - 43686523"),
        (L3, "Лифт L3 - 43686524"),
        (L4, "Лифт L4 - 43686525"),
        (L5, "Лифт L5 - 43686518"),
        (L6, "Лифт L6 - 43686520"),
        (L7, "Лифт L7 - 43686523"),
        (L8, "Лифт L8 - 43686524"),
        (L9, "Лифт L9 - 43686525"),
        (L10, "Лифт L10 - 43686529"),
        (L11, "Лифт L11 - 43686530"),
        (L12, "Лифт L12 - 43686527"),
        (L13, "Лифт L13 - 43686528"),
        (L14, "Лифт L14 - 43687022"),
        (L15, "Лифт L15 - 43687023"),
        (MSTK_L1, "Лифт МСТК L1 - 50046394"),
    ]

    elevator = models.CharField(
        choices=ELEVATORS, max_length=20, verbose_name="Лифт", help_text="Выбери лифт"
    )

    def __str__(self):
        return f"{self.get_elevator_display()}"

    class Meta:
        verbose_name = "Лифт"
        verbose_name_plural = "Лифты"


class Problem(models.Model):
    """
    Класс для записи проблем, и если проблема решена, то она помечена как решена
    """

    buildings = models.ForeignKey(
        Building,
        verbose_name="Здание",
        related_name="problems",
        on_delete=models.SET_NULL,
        null=True,
    )
    elevator = models.ForeignKey(
        Elevator, on_delete=models.CASCADE, verbose_name="Лифт", related_name="problems"
    )
    problem = models.TextField(verbose_name="Информация о проблеме")
    resolved = models.BooleanField(default=False, verbose_name="Решено")

    def __str__(self):
        return f"{self.problem} ({self.resolved})"

    class Meta:
        verbose_name = "Проблема"
        verbose_name_plural = "Проблемы"


class Replacement(models.Model):
    """
    Класс для записи, что стоит заменить
    """

    buildings = models.ForeignKey(
        Building,
        verbose_name="Здание",
        related_name="replacements",
        on_delete=models.CASCADE,
    )
    elevator = models.ForeignKey(
        Elevator, on_delete=models.CASCADE, verbose_name="Лифт"
    )
    info_problem = models.TextField(verbose_name="Что стоит заменить")
    resolved = models.BooleanField(default=False, verbose_name="Решено")

    def __str__(self):
        return self.info_problem

    class Meta:
        verbose_name = "Ремонт"
        verbose_name_plural = "Ремонты"


class TO(models.Model):
    """
    Класс проведения ТО на лифтах, какой лифт, и когда проводился
    """

    building = models.ForeignKey(
        Building,
        on_delete=models.SET_NULL,
        verbose_name="Здание",
        related_name="to",
        null=True,
    )
    elevator = models.ForeignKey(
        Elevator, on_delete=models.CASCADE, verbose_name="Лифт"
    )
    date = models.DateField(verbose_name="Дата проведения ТО")

    def __str__(self):
        return f"{self.elevator} - {self.date}"

    class Meta:
        verbose_name = "ТО"
        verbose_name_plural = "ТО"
