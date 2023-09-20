from django.db import models
from django.utils import timezone

class Item(models.Model):
    name = models.CharField(max_length=255)
    date_added = models.DateField(auto_now_add=True)
    description = models.TextField()
    amount = models.IntegerField(default=0)