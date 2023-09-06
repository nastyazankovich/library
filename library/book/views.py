from django.shortcuts import render
from .serializer import LibrarySerializer, BookSerializer
from .models import Library, Book
from rest_framework import viewsets


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class LibraryViewSet(viewsets.ModelViewSet):
    queryset = Library.objects.all()
    serializer_class = LibrarySerializer

# Create your views here.
