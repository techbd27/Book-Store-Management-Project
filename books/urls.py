from django.urls import path
from .views import homepage,add_book,delete_book
urlpatterns = [
    path('',homepage,name='homepage'),
    path('add_book/',add_book,name='add_book'),
    path('delete/<int:book_id>/',delete_book,name='delete_book')
]