from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from .views import *
from django.urls import path
from .api import BookListAPIView,LibraryListAPIView
urlpatterns = [
    path('book', BookListAPIView.as_view(), name='api_book'),
    path('library', LibraryListAPIView.as_view(), name='api_library')
]



# router = routers.DefaultRouter()
# router.register(r'books', BookViewSet)
# router.register(r'libraries', LibraryViewSet)

# urlpatterns = [
    # path('', include(router.urls)),
    # path('api-auth/', include('rest_framework.urls'))
# ]