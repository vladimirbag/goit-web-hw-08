import pika
from models import Contact

def send_email(contact):
    """Імітація надсилання email"""
    print(f"[Consumer] Sending email to {contact.fullname} ({contact.email})...")
    contact.sent = True
    contact.save()
    print(f"[Consumer] Email sent to {contact.fullname}")

def callback(ch, method, properties, body):
    contact_id = body.decode()
    contact = Contact.objects(id=contact_id).first()
    
    if contact and not contact.sent:
        send_email(contact)
    else:
        print(f"[Consumer] Contact {contact_id} already processed or not found")

    ch.basic_ack(delivery_tag=method.delivery_tag)

# Підключення до RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
channel = connection.channel()

# Переконуємось, що черга існує
channel.queue_declare(queue="email_queue")

# Отримуємо повідомлення з черги
channel.basic_consume(queue="email_queue", on_message_callback=callback)

print("[Consumer] Waiting for messages. To exit press CTRL+C")
channel.start_consuming()
