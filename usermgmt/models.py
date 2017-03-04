from django.db import models
from django.conf import settings
from django.contrib.auth.models import User


class Customer(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    picture = models.ImageField(
        upload_to='static/images/',
        null=True, blank=True)
