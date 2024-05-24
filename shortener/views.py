from django.shortcuts import render, redirect
from .forms import ShortenForm
from .models import URLShortener

def shorten(request, hash):
    hash = URLShortener.objects.get(id=hash)
    return redirect(hash.original_url)


def index(request):
    if request.method == "GET":
        return render(request, "index.html", {"form": ShortenForm()})
    else:
        url_shortener = URLShortener.objects.create(original_url=request.POST["url"])
        return render(
            request, "index.html", {"form": ShortenForm(), "id": url_shortener.id}
        )
