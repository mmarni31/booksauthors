from django.urls import path
from .views import BookListView, BookSearchView, AuthorSearchView
urlpatterns = [
    path('books/', BookListView.as_view(), name='book-list'),
    path('books/search/', BookSearchView.as_view(), name='book-search'),
    path('authors/search/', AuthorSearchView.as_view(), name='author-search'),
]





