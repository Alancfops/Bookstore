from django.shortcuts import render


def home_page(request):
    return render(request, "home_book/index.html")
