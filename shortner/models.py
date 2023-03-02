import random
import string

from django.db import models


def generate_short_code():
    """
    Generate a random 6 character code
    """
    short_code = ''.join(random.choices(string.ascii_lowercase + string.digits, k=6))
    return short_code


class ShortURL(models.Model):
    original_url = models.URLField()
    short_code = models.CharField(max_length=15, unique=True)
    num_clicks = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        """
        Override save method to generate short code before saving
        """
        if not self.pk:
            # Generate short code only for new instances
            self.short_code = generate_short_code()

        super().save(*args, **kwargs)

    def __str__(self):
        return self.short_code

    def get_short_url(self):
        return f'http://127.0.0.1:8000/{self.short_code}'

    def get_stats_url(self):
        """
        Return the URL for viewing statistics
        """
        return 'http://localhost:8000/stats/' + self.short_code




