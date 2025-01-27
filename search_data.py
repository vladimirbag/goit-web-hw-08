from models import Quote

# Пошук цитат за ім'ям автора
def find_by_author(name):
    quotes = Quote.objects(author__fullname=name)
    return [quote.quote for quote in quotes]

# Пошук цитат за тегом
def find_by_tag(tag):
    quotes = Quote.objects(tags=tag)
    return [quote.quote for quote in quotes]

# Пошук цитат за набором тегів
def find_by_tags(tags):
    tags_list = tags.split(',')
    quotes = Quote.objects(tags__in=tags_list)
    return [quote.quote for quote in quotes]

# Головна функція
def main():
    print("Enter a command (name:<author>, tag:<tag>, tags:<tag1,tag2>, exit):")
    while True:
        command = input("> ").strip()
        if command == "exit":
            print("Goodbye!")
            break

        try:
            if command.startswith("name:"):
                name = command.split(":", 1)[1]
                results = find_by_author(name)
            elif command.startswith("tag:"):
                tag = command.split(":", 1)[1]
                results = find_by_tag(tag)
            elif command.startswith("tags:"):
                tags = command.split(":", 1)[1]
                results = find_by_tags(tags)
            else:
                print("Invalid command. Try again.")
                continue

            if results:
                for quote in results:
                    print(quote)
            else:
                print("No quotes found.")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == '__main__':
    main()
