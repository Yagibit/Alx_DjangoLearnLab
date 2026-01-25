from bookshelf.models import Book
Book.objects.create(title="1984", author="George Orwell", publication_year=1949)

# Output: Book object (1)

book = Book.objects.get(title="1984")


print(book.title, book.author, book.publication_year)


# Output: 1984 George Orwell 1949

book.title = "Nineteen Eighty-Four"


book.save()


# Output: Title updated to Nineteen Eighty-Four

book.delete()


print(Book.objects.all())


# Output: <QuerySet []>