from django.db import models


class EscChoices(models.TextChoices):
    # E1
    E11 = "E11", "Е1-1 42422353"
    E12 = "E12", "Е1-2 42422354"
    E13 = "E13", "Е1-3 42422355"
    E14 = "E14", "Е1-4 42422356"
    E15 = "E15", "Е1-5 42422357"
    E16 = "E16", "Е1-6 42422358"
    # Е2
    E21 = "E21", "Е2-1 42422367"
    E22 = "E22", "Е2-2 42422368"
    E23 = "E23", "Е2-3 42422369"
    E24 = "E24", "Е2-4 42422370"
    E25 = "E25", "Е2-5 42422371"
    E26 = "E26", "Е2-6 42422372"
    # Е3
    E31 = "E31", "Е3-1 42422386"
    E32 = "E32", "Е3-2 42422387"
    E33 = "E33", "Е3-3 42422388"
    E34 = "E34", "Е3-4 42422389"
    E35 = "E35", "Е3-5 42422390"
    E36 = "E36", "Е3-6 42422391"
    # Е4
    E41 = "E41", "Е4-1 42422399"
    E42 = "E42", "Е4-2 42422400"
    E43 = "E43", "Е4-3 42422401"
    E44 = "E44", "Е4-4 42422402"
    E45 = "E45", "Е4-5 42422403"
    E46 = "E46", "Е4-6 42422404"
    # Е5
    E51 = "E51", "Е5-1 42422412"
    E52 = "E52", "Е5-2 42422413"
    E53 = "E53", "Е5-3 42422414"
    E54 = "E54", "Е5-4 42422415"
    E55 = "E55", "Е5-5 42422416"
    E56 = "E56", "Е5-6 42422417"
    # Е6
    E61 = "E61", "Е6-1 42422419"
    E62 = "E62", "Е6-2 42422420"
    E63 = "E63", "Е6-3 42422421"
    E64 = "E64", "Е6-4 42422422"
    # Е7
    E71 = "E71", "Е7-1 42422424"
    E72 = "E72", "Е7-2 42422425"
    E73 = "E73", "Е7-3 42422426"
    E74 = "E74", "Е7-4 42422427"
    # Е8
    E81 = "E81", "Е8-1 42422429"
    E82 = "E82", "Е8-2 42422430"
    # Е9
    E91 = "E91", "Е9-1 42422431"
    E92 = "E92", "Е9-2 42422432"


class Esc(models.Model):
    esc = models.CharField(
        choices=EscChoices.choices,
        max_length=14,
        default=EscChoices.E11,
        verbose_name="Эскалатор",
        help_text="Выберите эскалатор",
    )

    def __str__(self):
        return self.get_esc_display()

    class Meta:
        verbose_name = "Эскалатор"
        verbose_name_plural = "Эскалаторы"


class EscProblem(models.Model):
    esc = models.ForeignKey(Esc, on_delete=models.CASCADE, verbose_name="Эскалатор")
    problem = models.CharField(max_length=255, verbose_name="Проблема")
    create_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата проблемы")
    resolved = models.BooleanField(default=False, verbose_name="Решено")

    def __str__(self):
        return f"{self.esc} - {self.create_at}"

    class Meta:
        verbose_name = "Проблема"
        verbose_name_plural = "Проблемы"


class EscReplace(models.Model):
    esc = models.ForeignKey(Esc, on_delete=models.CASCADE, verbose_name="Эскалатор")
    replace = models.CharField(max_length=255, verbose_name="Заменить")
    create_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата замены")
    resolved = models.BooleanField(default=False, verbose_name="Решено")

    def __str__(self):
        return f"{self.esc} - {self.create_at}"

    class Meta:
        verbose_name = "Замена"
        verbose_name_plural = "Замены"


class EscTO(models.Model):
    esc = models.ForeignKey(Esc, on_delete=models.CASCADE, verbose_name="Эскалатор")
    create_at = models.DateTimeField(
        auto_now_add=True, verbose_name="Дата проведения ТО"
    )

    def __str__(self):
        return f"{self.esc} - {self.create_at}"

    class Meta:
        verbose_name = "ТО"
        verbose_name_plural = "ТО"
