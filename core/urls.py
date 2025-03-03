from django.contrib import admin
from django.urls import path
from home_book.views import home_page, img_view
from books_products.views import books_details

urlpatterns = [
    path("", home_page, name="home_page"),
    path("books/", books_details, name="books_details"),
    path("img/", img_view),
    path("admin/", admin.site.urls),
]
