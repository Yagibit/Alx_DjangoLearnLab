from bookshelf.models import Book

# Retrieve the book to be deleted
book = Book.objects.get(title="Nineteen Eighty-Four")

# Delete the book instance
book.delete()

# Confirm deletion by trying to retrieve all books
print(Book.objects.all())

# Expected Output: <QuerySet []>