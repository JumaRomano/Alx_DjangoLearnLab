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
