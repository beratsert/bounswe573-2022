from django.db import models

# Create your models here.

class Entries(models.Model):
    keyword = models.CharField(max_length=128)
    description = models.CharField(max_length=256)
    language = models.CharField(max_length=2)