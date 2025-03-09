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
    
    # New fields for dynamic content
    project_type = models.CharField(max_length=50, choices=[
        ('web', 'Web App'),
        ('desktop', 'Desktop App'),
        ('mobile', 'Mobile App'),
        ('other', 'Other'),
    ], default='web')
    version = models.CharField(max_length=10, default='1.0')
    status = models.CharField(max_length=20, choices=[
        ('completed', 'Completed'),
        ('in_progress', 'In Progress'),
        ('planned', 'Planned'),
    ], default='completed')
    tags = models.CharField(max_length=200, blank=True, help_text="Comma-separated tags, e.g., 'File Transfer, Desktop'")
    technologies = models.CharField(max_length=200, blank=True, help_text="Comma-separated tech stack, e.g., 'Django, JavaScript'")

    def get_tags_list(self):
        return [tag.strip() for tag in self.tags.split(',') if tag.strip()]

    def get_technologies_list(self):
        return [tech.strip() for tech in self.technologies.split(',') if tech.strip()]

    def __str__(self):
        return self.title

class ProjectMedia(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='media')
    image = models.ImageField(upload_to='project_media/', null=True, blank=True)
    caption = models.CharField(max_length=100, blank=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.project.title} - {self.caption or 'Image'}"

class Feedback(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.subject}"