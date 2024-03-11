from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone
from datetime import timedelta

def default_date_created():
    return timezone.now()

def default_end_date():
    return timezone.now() + timedelta(days=45)

class Project (models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    goal = models.IntegerField()
    image = models.URLField()
    is_open = models.BooleanField()
    date_created = models.DateTimeField(default=default_date_created)
    end_date = models.DateTimeField(default=default_end_date)
    owner = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='owned_projects'
    )

class Pledge(models.Model):
    amount = models.IntegerField()
    comment = models.CharField(max_length=200)
    anonymous = models.BooleanField()
    date_created = models.DateTimeField(auto_now_add=True)
    project = models.ForeignKey(
        'Project',
        on_delete=models.CASCADE,
        related_name='pledges'
    )
    supporter = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='pledges'
    )