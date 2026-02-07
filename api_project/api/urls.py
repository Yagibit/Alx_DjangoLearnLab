from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookList, BookViewSet

# Create a router and register our viewset with it.
router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')

urlpatterns = [
    # Route for the existing BookList view (Task 2)
    path('books/', BookList.as_view(), name='book-list'),

    # Route for the NEW BookViewSet (Task 3 CRUD)
    path('', include(router.urls)),
]