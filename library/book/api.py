from rest_framework.generics import ListAPIView
from . import serializer
from . import models


class BookListAPIView(ListAPIView):
    serializer_class = serializer.BookSerializer

    def get_queryset(self):
        return models.Book.objects.all()


class LibraryListAPIView(ListAPIView):
    serializer_class = serializer.LibrarySerializer

    def get_queryset(self):
        return models.Library.objects.all()