from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, Http404
from .models import ShortURL
from .forms import ShortURLForm
import string
import random


def index(request):
    form = ShortURLForm(request.POST or None)
    if form.is_valid():
        url = form.cleaned_data['url']
        short_code = generate_short_code()
        short_url = ShortURL(url=url, short_code=short_code)
        short_url.save()
        return redirect('shortener:short_url_created', short_code=short_code)
    return render(request, 'index.html', {'form': form})


def generate_short_code(request):
    if request.method == 'POST':
        form = ShortURLForm(request.POST)
        if form.is_valid():
            url = form.cleaned_data['url']
            short_url = ShortURL(original_url=url)
            short_url.save()
            return render(request, 'shortened.html', {'short_url': short_url})
    else:
        form = ShortURL()

    return render(request, 'index.html', {'form': form})


def short_url_created(request, short_code):
    short_url = get_object_or_404(ShortURL, short_code=short_code)
    context = {
        'short_url': short_url
    }
    return render(request, 'short_url_created.html', context)


def redirect_original(request, short_code):
    try:
        short_url = ShortURL.objects.get(short_code=short_code)
        return redirect(short_url.original_url)
    except ShortURL.DoesNotExist:
        raise Http404('ShortURL does not exist')

