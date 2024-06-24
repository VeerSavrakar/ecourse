from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    email = models.EmailField(max_length=254, unique=True)
    # Add any other additional fields you want for your custom user model
    # For example:
    # date_of_birth = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.username
