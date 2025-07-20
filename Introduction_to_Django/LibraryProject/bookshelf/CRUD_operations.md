book = Book.objects.create(title="The Great Gatsby", author="F. Scott Fitzgerald", publication_year=1925)

book

# <Book: The Great Gatsby>


Book.objects.all()

# <QuerySet [<Book: The Great Gatsby>]>

book = Book.objects.get(title="The Great Gatsby")

book.title, book.author, book.publication_year

# ('The Great Gatsby', 'F. Scott Fitzgerald', 1925)

ook.title = "Dune"

book.save()

book.title

# 'Dune'

# Delete Book

from bookshelf.models import Book

book = Book.objects.create(title="The Great Gatsby", author="F. Scott Fitzgerald", publication_year=1925)

book

\# <Book: The Great Gatsby>



book.delete()

Book.objects.all()

\# <QuerySet \[]>
