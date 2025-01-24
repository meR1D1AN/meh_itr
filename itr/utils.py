import re


def sanitize_filename(filename):
    # Удаляем недопустимые символы
    return re.sub(r'[<>:"/\\|?*]', "_", filename)
