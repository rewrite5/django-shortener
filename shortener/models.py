from django.db import models

# Create your models here.
# class URLShortener(models.Model):
#     hash = models.CharField(max_length=7, unique=True)
#     original_url = models.URLField()

#     def __str__(self):
#         return self.hash

from shortuuid.django_fields import ShortUUIDField


class URLShortener(models.Model):
    # A primary key ID of length 16 and a short alphabet.
    id = ShortUUIDField(
        length=7,
        max_length=7,
        prefix="",
        alphabet="abcdefg1234567890",
        primary_key=True,
    )
    original_url = models.URLField()

    def __str__(self):
        return f"http://localhost:8000/s/{self.id}"
