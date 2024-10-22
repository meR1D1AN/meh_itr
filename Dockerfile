FROM python:3.12

WORKDIR /app

# Копируем только файл с зависимостями
COPY pyproject.toml poetry.lock ./

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Копируем остальной код проекта
COPY . .