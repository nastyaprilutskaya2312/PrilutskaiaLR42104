#!/bin/bash

echo "========================================="
echo "  Развертывание приложения контроля"
echo "  целостности программного обеспечения"
echo "========================================="

# Установка зависимостей
echo "1. Установка зависимостей..."
pip install -r requirements.txt

# Выполнение миграций базы данных
echo "2. Выполнение миграций..."
python manage.py makemigrations
python manage.py migrate

# Сбор статических файлов (если есть)
echo "3. Сбор статических файлов..."
python manage.py collectstatic --noinput

# Запуск сервера
echo "4. Запуск сервера разработки..."
echo "Приложение будет доступно по адресу:"
echo "   http://localhost:8000/integrity/"
python manage.py runserver 0.0.0.0:8000