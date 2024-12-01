from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Book
from .serializers import BookSerializer

class BookListView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
class BookListView(generics.ListCreateAPIView):
    ...
    def perform_create(self, serializer):
        # Customize behavior during book creation
        serializer.save()

class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    ...
    def perform_update(self, serializer):
        # Add custom logic for updates
        serializer.save()
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class BookListView(generics.ListCreateAPIView):
    ...
    permission_classes = [IsAuthenticatedOrReadOnly]  # Read-only for unauthenticated users

class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    ...
    permission_classes = [IsAuthenticatedOrReadOnly]
"""
BookListView:
- Handles listing all books and creating a new book.
- Only authenticated users can create books.
- Read-only access is allowed for unauthenticated users.

BookDetailView:
- Handles retrieving, updating, and deleting a specific book by ID.
- Only authenticated users can update or delete books.
- Read-only access is allowed for unauthenticated users.
"""
from rest_framework import generics
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from .models import Book
from .serializers import BookSerializer

class BookListView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['title', 'author__name', 'publication_year']
    search_fields = ['title', 'author__name']
    ordering_fields = ['title', 'publication_year']
    ordering = ['title']  # Default ordering
"""
BookListView:
- Supports filtering by title, author name, and publication year.
- Allows text search on title and author name.
- Supports ordering by title and publication year.
"""
from rest_framework.generics import CreateAPIView, UpdateAPIView, DestroyAPIView
from .models import Book
from .serializers import BookSerializer

class BookCreateView(CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookUpdateView(UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookDeleteView(DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
from rest_framework.permissions import IsAuthenticated

class BookCreateView(CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

class BookUpdateView(UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

class BookDeleteView(DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated