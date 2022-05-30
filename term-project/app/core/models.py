from django.db import models
from django.conf import settings
from django.utils.text import slugify
from django.urls import reverse
from ckeditor.fields import RichTextField
import time

class Learningspace(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    desc = RichTextField(blank=True, null = True)
    created_at = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name= 'learningspaces')

    def save(self, *args, **kwargs):
        if self.pk is None:
            self.slug = slugify(self.title) + '-' + time.strftime('%Y%m%d%H%M%S')
        super(Learningspace, self).save(*args, **kwargs)

    def get_absolute_url(self): 
        return reverse('home')
        
    def __str__(self):
        return self.title

class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    slug = models.ForeignKey(Learningspace, on_delete=models.CASCADE)
    desc = RichTextField(blank=True, null = True)
    created_at = models.DateTimeField(auto_now_add=True)

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, null=True, on_delete = models.CASCADE)
    bio = models.TextField()
    profile_pic = models.ImageField(null=True, blank=True, upload_to="images/profile/")

    def __str__(self):
        return str(self.user)