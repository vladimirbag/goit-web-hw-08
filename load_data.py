import json
from models import Author, Quote

# Функція для завантаження авторів
def load_authors(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        data = json.load(file)
        for author_data in data:
            author = Author(**author_data)
            author.save()

# Функція для завантаження цитат
def load_quotes(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        data = json.load(file)
        for quote_data in data:
            author_name = quote_data.pop('author')
            author = Author.objects(fullname=author_name).first()
            if author:
                quote = Quote(author=author, **quote_data)
                quote.save()

# Виклик функцій завантаження
load_authors('authors.json')
load_quotes('qoutes.json')
