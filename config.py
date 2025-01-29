import os
from dotenv import load_dotenv

# Завантажуємо змінні з .env файлу
load_dotenv()

# Читаємо змінні середовища
RABBITMQ_USER = os.getenv("RABBITMQ_USER")
RABBITMQ_PASSWORD = os.getenv("RABBITMQ_PASSWORD")
RABBITMQ_HOST = os.getenv("RABBITMQ_HOST", "localhost")  # Значення за замовчуванням
RABBITMQ_PORT = int(os.getenv("RABBITMQ_PORT", 5672))
RABBITMQ_VHOST = os.getenv("RABBITMQ_VHOST", "/")
MONGODB_URI = os.getenv("MONGODB_URI")