# Delete Book

from bookshelf.models import Book

book = Book.objects.create(title="The Great Gatsby", author="F. Scott Fitzgerald", publication_year=1925)

book

\# <Book: The Great Gatsby>



book.delete()

Book.objects.all()

\# <QuerySet \[]>
