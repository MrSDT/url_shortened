from django.db import models
from django.db import models
import string
import random


class ShortURL(models.Model):
    original_url = models.URLField(max_length=2048)
    short_code = models.CharField(max_length=16, unique=True)
    clicks = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        if not self.pk:
            # Generate a unique short code
            while True:
                short_code = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
                if not ShortURL.objects.filter(short_code=short_code).exists():
                    self.short_code = short_code
                    break
        super().save(*args, **kwargs)

    def get_short_url(self):
        return f"http://localhost:8000/{self.short_code}"



