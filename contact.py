from mongoengine import Document, StringField, BooleanField, connect

# Підключення до бази даних
connect(host="mongodb://localhost:27017/email_sender")

class Contact(Document):
    fullname = StringField(required=True)
    email = StringField(required=True, unique=True)
    sent = BooleanField(default=False)  # Чи надіслано повідомлення

    def __str__(self):
        return f"{self.fullname} ({self.email}) - Sent: {self.sent}"
