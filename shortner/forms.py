from django import forms
from .models import ShortURL


class ShortURLForm(forms.ModelForm):
    class Meta:
        model = ShortURL
        fields = ['original_url']
        labels = {
            'original_url': 'لینک شما:'
        }
        widgets = {
            'original_url': forms.TextInput(attrs={'placeholder': 'لینک خودرا کوتاه کنید',
                                                   'class': 'form-control'})
        }
