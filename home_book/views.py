from django.shortcuts import render


def home_page(request):
    return render(request, "home_book/index.html")


def img_view(request):
    content = {
        "images": {
            "image_url": "https://m.media-amazon.com/images/I/910Om0O1zCL._AC_UF1000,1000_QL80_.jpg"
        }
    }
    return render(request, "home_book/index.html", content)
