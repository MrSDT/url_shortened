from django import forms
from .models import ShortURL


class ShortURLForm(forms.ModelForm):
    class Meta:
        model = ShortURL
        fields = ['original_url']
        widgets = {
            'original_url': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'Enter a URL to shorten'}),
        }
