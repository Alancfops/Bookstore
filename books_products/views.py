from django.shortcuts import render


def books_details(request):
    return render(request, "books_products/index.html")
