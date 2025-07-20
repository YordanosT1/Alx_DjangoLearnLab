# Delete Book

from bookshelf.models import Book

book = Book.objects.create(title="1984", author="George Orwell", publication\_year=1949)

book

\# <Book: 1984>



book.delete()

Book.objects.all()

\# <QuerySet \[]>

Book.objects.all()

\# <QuerySet \[]>
