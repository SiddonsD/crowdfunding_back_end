from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    username = models.CharField(max_length=200, unique=True, null=False, blank=False, verbose_name='username')
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=256, unique=True, verbose_name='email')

    def __str__(self):
        return self.username
    
    def delete (self, *args, **kwargs):
        print (f"User {self.username} is about to be deleted.")
        super().delete(*args, **kwargs)