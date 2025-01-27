from mongoengine import Document, StringField, ReferenceField, ListField, connect

# Підключення до хмарної MongoDB
connect(host='mongodb+srv://<username>:<password>@cluster.mongodb.net/<database>?retryWrites=true&w=majority')

# Модель для авторів
class Author(Document):
    fullname = StringField(required=True, unique=True)
    born_date = StringField()
    born_location = StringField()
    description = StringField()

# Модель для цитат
class Quote(Document):
    tags = ListField(StringField())
    author = ReferenceField(Author, reverse_delete_rule=2)  # Reference to Author
    quote = StringField(required=True)
