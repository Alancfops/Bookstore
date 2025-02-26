from django.contrib import admin
from django.urls import path
from home_book.views import home_page

urlpatterns = [
    path("home/", home_page),
    path("admin/", admin.site.urls),
]
