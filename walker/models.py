from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class WalkEntry(models.Model):
    date = models.DateField(auto_now=True)
    distance = models.CharField(max_length=5)
    time = models.CharField(max_length=5)
    weight = models.CharField(max_length=4)
    image_url = models.CharField(max_length=600, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name="walks")

    def __str__(self):
        return self.distance