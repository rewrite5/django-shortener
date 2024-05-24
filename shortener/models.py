from django.db import models
from shortuuid.django_fields import ShortUUIDField
class URLShortener(models.Model):
    id = ShortUUIDField(
        length=7,
        max_length=7,
        prefix="",
        alphabet="abcdefg1234567890",
        primary_key=True,
    )
    original_url = models.URLField(max_length=2048)

    def __str__(self):
        return self.id
