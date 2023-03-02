from django import forms
from .models import ShortURL


class ShortURLForm(forms.ModelForm):
    url = forms.URLField(label='URL', required=True)

    class Meta:
        model = ShortURL
        fields = ['original_url']
        widgets = {
            'original_url': forms.TextInput(attrs={'placeholder': 'Paste a long URL to shorten it', 'class': 'form-control'})
        }
