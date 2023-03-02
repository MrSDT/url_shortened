import random
import string

from django.db import models
from django.urls import reverse


def generate_short_code():
    """
    Generate a random 6 character code
    """
    short_code = ''.join(random.choices(string.ascii_lowercase + string.digits, k=6))
    return short_code


class ShortURL(models.Model):
    original_url = models.URLField(max_length=1000)
    short_code = models.CharField(max_length=15, unique=True, blank=True)
    num_clicks = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.original_url

    def get_short_url(self):
        return reverse('redirect_original', args=[self.short_code])

    def get_stats_url(self):
        return reverse('short_url_stats', args=[self.short_code])

    def save(self, *args, **kwargs):
        if not self.pk:
            # This code only runs if the object is being created for the first time
            self.short_code = generate_short_code()

        super().save(*args, **kwargs)
