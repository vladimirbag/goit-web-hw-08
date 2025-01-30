import os
from dotenv import load_dotenv
from mongoengine import connect

# Завантажуємо змінні середовища
load_dotenv()

# Отримуємо значення змінної
MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017/email_sender")

# Підключення до бази даних
connect(host=MONGO_URI)

print(f"✅ Підключено до MongoDB: {MONGO_URI}")
