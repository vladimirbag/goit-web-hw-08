import pika
from faker import Faker
from models import Contact

# Генеруємо контакти
fake = Faker()

# Підключення до RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
channel = connection.channel()

# Створюємо чергу, якщо її ще немає
channel.queue_declare(queue="email_queue")

# Генеруємо 10 фейкових контактів
for _ in range(10):
    contact = Contact(fullname=fake.name(), email=fake.email())
    contact.save()  # Збереження в MongoDB
    contact_id = str(contact.id)

    # Відправлення повідомлення в чергу RabbitMQ
    channel.basic_publish(exchange="", routing_key="email_queue", body=contact_id)
    print(f"[Producer] Contact {contact.fullname} added to queue")

connection.close()
