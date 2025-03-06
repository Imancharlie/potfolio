# projects/views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.http import FileResponse
from django.shortcuts import render, redirect
from .models import Project, Feedback
from django.contrib import messages
from django.http import JsonResponse

def home(request):
    projects = Project.objects.all().order_by('-created_at')

    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        if name and email and subject and message:
            Feedback.objects.create(name=name, email=email, subject=subject, message=message)
            return redirect('home')

    return render(request, 'projects/home.html', {'projects': projects})

def project_detail(request, slug):
    project = get_object_or_404(Project, slug=slug)
        
    return render(request, 'projects/project_detail.html', {'project': project})

def download_file(request, slug):
    project = get_object_or_404(Project, slug=slug)
    if project.download_file:
        return FileResponse(project.download_file.open(), as_attachment=True)
    return redirect('project_detail', slug=slug)