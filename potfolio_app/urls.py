# projects/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('project/<slug:slug>/', views.project_detail, name='project_detail'),
    path('project/<slug:slug>/download/', views.download_file, name='download_file'),
]
