from django.contrib import admin

from itr.models import Employee, Customer, WorkDay, Vacation


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ("id", "last_name", "first_name", "middle_name", "position")

    def get_customers(self, obj):
        return ", ".join([customer.customer_name for customer in obj.customers.all()])
    get_customers.short_description = 'Заказчики'


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "customer_name",
        "address_customer",
        "salary",
        "work_schedule",
        "responsible_person",
        "contact_phone",
        "created_by",
    )

@admin.register(WorkDay)
class WorkDayAdmin(admin.ModelAdmin):
    list_display = ("employee", "date", "salary")

@admin.register(Vacation)
class VacationAdmin(admin.ModelAdmin):
    list_display = ("user", "employee", "start_date", "end_date", "status")
