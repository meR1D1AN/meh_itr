from calendar import monthrange

from itr.models import Employee, WorkDay


def get_workdays(customer, current_month, current_year):
    employees = Employee.objects.filter(customer=customer)
    workdays = WorkDay.objects.filter(employee__in=employees, date__year=current_year, date__month=current_month)
    employee_workdays = {}
    for workday in workdays:
        if workday.employee not in employee_workdays:
            employee_workdays[workday.employee] = []
        employee_workdays[workday.employee].append(workday.date.day)
    return employee_workdays


def get_month_days(current_month, current_year):
    _, days_in_month = monthrange(current_year, current_month)
    return days_in_month
