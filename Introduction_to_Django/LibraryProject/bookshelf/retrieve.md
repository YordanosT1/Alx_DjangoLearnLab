Book.objects.all()

# <QuerySet [<Book: The Great Gatsby>]>

book = Book.objects.get(title="The Great Gatsby")

book.title, book.author, book.publication_year

# ('The Great Gatsby', 'F. Scott Fitzgerald', 1925)