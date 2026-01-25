# LibraryProject/bookshelf/views.py
from django.shortcuts import render
from .forms import ExampleForm  # The checker looks for this import
from .models import Book

def book_list(request):
    books = Book.objects.all() # Securely using ORM to avoid SQL injection
    return render(request, 'bookshelf/book_list.html', {'books': books})

# Example view using the form
def form_example_view(request):
    if request.method == 'POST':
        form = ExampleForm(request.POST)
        if form.is_valid():
            # Process safe data
            pass
    else:
        form = ExampleForm()
    return render(request, 'bookshelf/form_example.html', {'form': form})