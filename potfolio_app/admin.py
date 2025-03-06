# projects/admin.py
from django.contrib import admin
from .models import Project, Feedback

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'has_download', 'external_url')
    prepopulated_fields = {'slug': ('title',)}
    
admin.site.register(Feedback)