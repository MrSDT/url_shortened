from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .models import ShortURL
from .forms import ShortURLForm


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
            return redirect(reverse('shortener:shorten_url_created', args=[short_url.short_code]))
    else:
        form = ShortURLForm()

    return render(request, 'index.html', {'form': form, 'title': title})


def redirect_original(request, short_code):
    """
    Redirect to original URL based on short code
    """
    short_url = get_object_or_404(ShortURL, short_code=short_code)
    short_url.num_clicks += 1
    short_url.save()
    return redirect(short_url.original_url)


def shorten_url(request):
    """
    Render page with short URL created from original URL
    """
    short_url = None
    if request.method == 'POST':
        form = ShortURLForm(request.POST)
        if form.is_valid():
            url = form.cleaned_data['url']
            short_url = ShortURL(original_url=url)
            short_url.save()
            return redirect(reverse('stats', kwargs={'short_code': short_url.short_code}))

    form = ShortURLForm()
    return render(request, 'shorten.html', {'form': form, 'short_url': short_url})


def shorten_url_created(request, short_code):
    """
    Render page showing the original and shortened URLs, as well as the number of clicks
    """
    short_url = get_object_or_404(ShortURL, short_code=short_code)
    return render(request, 'stats.html', {'short_url': short_url})
