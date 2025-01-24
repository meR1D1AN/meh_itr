import calendar
from datetime import datetime
from django.shortcuts import get_object_or_404, redirect, render

from itr.forms import MonthYearForm
from itr.models import Customer, WorkDay


def calculate_daily_salary(
    day, month_days, monthly_salary, work_schedule, customer, year=None, month=None
):
    """
    Рассчитывает стоимость одной смены для указанного дня на основе графика работы.
    """
    if work_schedule == "2/2":
        start_day = customer.start_work.day

        # Определяем, какой график использовать на основе дня начала работы
        if start_day % 2 == 1:  # Нечетные дни (1, 3, 5, ...)
            if month_days == 30:
                if day in {1, 2, 5, 6, 9, 10, 13, 14, 17, 18, 21, 22, 25, 26, 29, 30}:
                    return monthly_salary / 16
                elif day in {3, 4, 7, 8, 11, 12, 15, 16, 19, 20, 23, 24, 27, 28}:
                    return monthly_salary / 14
            elif month_days == 31:
                if day in {1, 2, 5, 6, 9, 10, 13, 14, 17, 18, 21, 22, 25, 26, 29, 30}:
                    return monthly_salary / 16
                elif day in {3, 4, 7, 8, 11, 12, 15, 16, 19, 20, 23, 24, 27, 28, 31}:
                    return monthly_salary / 15
        else:  # Четные дни (2, 4, 6, ...)
            if month_days == 30:
                if day in {1, 4, 5, 8, 9, 12, 13, 16, 17, 20, 21, 24, 25, 28, 29}:
                    return monthly_salary / 15
                elif day in {2, 3, 6, 7, 10, 11, 14, 15, 18, 19, 22, 23, 26, 27, 30}:
                    return monthly_salary / 15
            elif month_days == 31:
                if day in {1, 4, 5, 8, 9, 12, 13, 16, 17, 20, 21, 24, 25, 28, 29}:
                    return monthly_salary / 15
                elif day in {
                    2,
                    3,
                    6,
                    7,
                    10,
                    11,
                    14,
                    15,
                    18,
                    19,
                    22,
                    23,
                    26,
                    27,
                    30,
                    31,
                }:
                    return monthly_salary / 16

    elif work_schedule == "1/3":
        if month_days == 31:
            # Дни, кратные 4: 4, 8, 12, 16, 20, 24, 28 → salary / 7
            if day % 4 == 0:
                return monthly_salary / 7
            else:
                return monthly_salary / 8
        elif month_days == 30:
            # Дни, где (day-1) % 4 < 2: 1,2,5,6,9,10,...29,30 → salary / 7
            if (day - 1) % 4 < 2:
                return monthly_salary / 7
            else:
                return monthly_salary / 8
        elif month_days == 28:
            # Все дни делятся на 7
            return monthly_salary / 7
        
    elif work_schedule == "5/2":
        # Определяем количество рабочих дней в месяце
        if year is not None and month is not None:
            working_days = sum(
                1
                for day in range(1, month_days + 1)
                if calendar.weekday(year, month, day) < 5
            )  # Пн-Пт
            if working_days > 0:  # Избегаем деления на ноль
                return monthly_salary / working_days
    elif work_schedule == "6/1":
        # Определяем количество рабочих дней в месяце, исключая воскресенья
        if year is not None and month is not None:
            working_days = sum(
                1
                for day in range(1, month_days + 1)
                if calendar.weekday(year, month, day) != 6
            )  # Не воскресенье
            if working_days > 0:  # Избегаем деления на ноль
                return monthly_salary / working_days
    return 0  # По умолчанию возвращаем 0, если график неизвестен


def calculate_salary(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    employees = customer.employees.all()

    if request.method == "POST":
        month_year_form = MonthYearForm(request.POST)
        if month_year_form.is_valid():
            month = int(month_year_form.cleaned_data["month"])
            year = int(month_year_form.cleaned_data["year"])

            # Обработка сохранения при нажатии кнопки "Сохранить"
            if "save" in request.POST:
                days_in_month = calendar.monthrange(year, month)[1]
                days_in_month_list = [day for day in range(1, days_in_month + 1)]

                for employee in employees:
                    for day in days_in_month_list:
                        date = datetime(year, month, day)
                        is_workday = f"workday_{employee.id}_{day}" in request.POST
                        if is_workday:
                            daily_salary = calculate_daily_salary(
                                day,
                                days_in_month,
                                customer.salary,
                                customer.work_schedule,
                                customer,
                                year,
                                month,
                            )
                            # Обновляем или создаем запись рабочего дня с зарплатой
                            WorkDay.objects.update_or_create(
                                employee=employee,
                                date=date,
                                defaults={"salary": daily_salary},
                            )
                        else:
                            # Удаляем запись, если чекбокс снят
                            WorkDay.objects.filter(
                                employee=employee, date=date
                            ).delete()
                # Перенаправляем на ту же страницу для предотвращения повторной отправки формы
                return redirect("itr:calculate_salary", pk=pk)
    else:
        # При GET-запросе устанавливаем текущий месяц и год по умолчанию
        current_date = datetime.now()
        month = current_date.month
        year = current_date.year
        month_year_form = MonthYearForm(initial={"month": month, "year": year})

    # Общая логика для формирования данных для таблицы
    days_in_month = calendar.monthrange(year, month)[1]
    days_in_month_list = [day for day in range(1, days_in_month + 1)]

    salary_data = []
    for employee in employees:
        workdays = WorkDay.objects.filter(
            employee=employee, date__year=year, date__month=month
        ).order_by("date")
        workday_days = [workday.date.day for workday in workdays]
        total_shifts = len(workday_days)
        total_salary = sum(workday.salary for workday in workdays)

        total_salary = round(total_salary)

        # Сохраняем данные для отображения в шаблоне
        salary_data.append(
            {
                "employee": employee,
                "workday_days": workday_days,
                "total_shifts": total_shifts,
                "total_salary": total_salary,
            }
        )
    # Сортировка salary_data по фамилии
    salary_data = sorted(salary_data, key=lambda x: x["employee"].last_name)

    weekends = [
        day for day in days_in_month_list if datetime(year, month, day).weekday() >= 5
    ]

    context = {
        "customer": customer,
        "employees": employees,
        "month_year_form": month_year_form,
        "days_in_month": days_in_month_list,
        "salary_data": salary_data,
        "weekends": weekends,
    }
    return render(request, "itr/calculate_salary.html", context)
