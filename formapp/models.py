from unicodedata import name
from django.db import models

# Create your models here.
class Personal(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
