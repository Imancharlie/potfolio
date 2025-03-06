# projects/models.py
from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    short_description = models.CharField(max_length=200)
    thumbnail = models.ImageField(upload_to='project_thumbnails/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    # For projects with downloadable files
    has_download = models.BooleanField(default=False)
    download_file = models.FileField(upload_to='downloads/', null=True, blank=True)
    
    # For projects with external links
    external_url = models.URLField(null=True, blank=True)
    
    def __str__(self):
        return self.title

class Feedback(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.subject}"
