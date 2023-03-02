import random
import string
from django.shortcuts import render, redirect
from django.urls import reverse
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


def redirect_original(request, short_code):
    """
    Redirect to original URL based on short code
    """
    try:
        short_url = ShortURL.objects.get(short_code=short_code)
        short_url.num_clicks += 1
        short_url.save()
        return redirect(short_url.original_url)
    except ShortURL.DoesNotExist:
        return render(request, '404.html')


def short_url_created(request, short_code):
    """
    Render page showing the original and shortened URLs, as well as the number of clicks
    """
    short_url = ShortURL.objects.get(short_code=short_code)
    return render(request, 'stats.html', {'short_url': short_url})


def generate_short_code():
    """
    Generate a unique short code for a URL
    """
    length = 6
    while True:
        short_code = ''.join(random.choices(string.ascii_letters + string.digits, k=length))
        try:
            ShortURL.objects.get(short_code=short_code)
        except ShortURL.DoesNotExist:
            return short_code


def shorten_url(request):
    if request.method == 'POST':
        form = ShortURLForm(request.POST)
        if form.is_valid():
            url = form.cleaned_data['url']
            short_url = ShortURL(original_url=url)
            short_url.save()
            return render(request, 'shortened.html', {'short_url': short_url})
    else:
        form = ShortURLForm()

    return render(request, 'index.html', {'form': form})
