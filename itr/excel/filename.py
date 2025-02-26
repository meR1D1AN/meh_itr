def get_filename(customer, month_name_ru, current_year):
    from urllib.parse import quote

    from itr.utils import sanitize_filename

    sanitized_name = sanitize_filename(customer.customer_name)
    filename = f"График {sanitized_name} {month_name_ru}_{current_year}.xlsx"
    encoded_filename = quote(filename)
    return encoded_filename
