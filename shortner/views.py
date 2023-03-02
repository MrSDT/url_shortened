from django.shortcuts import render
from .forms import ShortURLForm
from .models import ShortURL


def index(request):
    """
    Render index page with form for submitting URL
    """
    title = 'URL Shortener'
    if request.method == 'POST':
        form = ShortURLForm(request.POST)
        if form.is_valid():
            url = form.cleaned_data['url']
            short_url = ShortURL(original_url=url)
            short_url.save()
            return render(request, 'shortened.html', {'short_url': short_url})
    else:
        form = ShortURLForm()

    return render(request, 'index.html', {'form': form, 'title': title})


def short_url_created(request, short_code):
    """
    Render page showing the original and shortened URLs, as well as the number of clicks
    """
    short_url = ShortURL.objects.get(short_code=short_code)
    return render(request, 'shortened.html', {'short_url': short_url})


def shorten_url(request):
    """
    Shorten URL and create new ShortURL object
    """
    if request.method == 'POST':
        form = ShortURLForm(request.POST)
        if form.is_valid():
            url = form.cleaned_data['url']
            short_url = ShortURL(original_url=url)
            short_url.save()
            short_code = str(short_url.id)
            short_url.short_code = short_code
            short_url.save()
            return render(request, 'shortened.html', {'short_url': short_url})
    else:
        form = ShortURLForm()

    return render(request, 'index.html', {'form': form})

