from datetime import datetime


def get_current_month_year(request):
    selected_month = request.GET.get("month")
    selected_year = request.GET.get("year")
    if selected_month and selected_year:
        current_month = int(selected_month)
        current_year = int(selected_year)
    else:
        current_date = datetime.now()
        current_month = current_date.month
        current_year = current_date.year
    return current_month, current_year
