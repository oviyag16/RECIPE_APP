from django.db import models
from django.contrib.auth.models import User

# Define your models here

class Recipe(models.Model):
    VEG = 'VEG'
    NON_VEG = 'NON-VEG'
    TYPE_CHOICES = [
        (VEG, 'Vegetarian'),
        (NON_VEG, 'Non-Vegetarian'),
    ]

    title = models.CharField(max_length=100)
    description = models.TextField()
    type = models.CharField(max_length=8, choices=TYPE_CHOICES, default=VEG)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title