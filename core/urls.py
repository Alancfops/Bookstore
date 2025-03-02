from django.contrib import admin
from django.urls import path
from home_book.views import home_page, img_view

urlpatterns = [
    path("", home_page),
    path("img/", img_view),
    path("admin/", admin.site.urls),
]
