from django.db import models
from django.conf import settings
# Create your models here.

class Profile(models.Model):
    user_profile = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)