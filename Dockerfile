FROM python:3.12.9

WORKDIR /app

# Копируем только файл с зависимостями
COPY pyproject.toml ./

# Устанавливаем Poetry и зависимости
RUN pip install poetry && \
    poetry config virtualenvs.create false && \
    poetry install --no-root

# Копируем остальной код проекта
COPY . .

# Собираем статические файлы при сборке образа
RUN python manage.py collectstatic --noinput
