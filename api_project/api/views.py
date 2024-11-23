from django.shortcuts import render
generics.ListAPIView
# Create your views here.
from rest_framework .generics import ListAPIView
from .models import Book
from .serializers import BookSerializer
from rest_framework.viewsets import ModelViewSet

class BookList(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
class BookViewSet(ModelViewSet):
    """
    A ViewSet for CRUD operations on the Book model.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer