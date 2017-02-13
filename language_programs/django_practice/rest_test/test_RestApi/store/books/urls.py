from django.conf.urls import url
from books.views import BooksView

urlpatterns = [
    url(r'^$', BooksView.as_view(), name='book-get-post-patch'),
    ]