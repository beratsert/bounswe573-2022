from django.db import models
from django.conf import settings
from django.utils.text import slugify
from django.urls import reverse

import time


class Workspace(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title) + '-' + time.strftime('%Y%m%d%H%M%S')
        super(Workspace, self).save(*args, **kwargs)

    def get_absolute_url(self): 
        return reverse('home')
        
    def __str__(self):
        return self.title

class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    workspace = models.ForeignKey(Workspace, on_delete=models.CASCADE)
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)