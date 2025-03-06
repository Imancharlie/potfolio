# scripts/initialize_projects.py
import os
from django.core.files.images import ImageFile
from django.core.files import File
from potfolio_app.models import Project
from django.utils.text import slugify

def run():
    # Clear existing projects
    Project.objects.all().delete()
    
    # Create WiFile+ project
    wifile = Project(
        title="WiFile+",
        slug="wifile-plus",
        description="""
        <h3>WiFile+ - Wireless File Transfer Application</h3>
        <p>WiFile+ is an innovative wireless file transfer application that allows for seamless file sharing between devices on the same network. It eliminates the need for cables, Bluetooth connections, or cloud services.</p>
        
        <h4>Key Features:</h4>
        <ul>
            <li>Fast and secure wireless file transfer</li>
            <li>Cross-platform compatibility (Windows, macOS, Linux)</li>
            <li>No size limitations for file transfers</li>
            <li>Simple and intuitive user interface</li>
            <li>No internet connection required (works on local network)</li>
            <li>End-to-end encryption for all transfers</li>
        </ul>
        
        <h4>System Requirements:</h4>
        <ul>
            <li>Any modern operating system (Windows 7+, macOS 10.12+, Ubuntu 18.04+)</li>
            <li>Minimum 2GB RAM</li>
            <li>10MB disk space</li>
            <li>Network connection (Wi-Fi or Ethernet)</li>
        </ul>
        
        <h4>Installation Instructions:</h4>
        <p>Simply download the zip file, extract it, and run the installer. The application will guide you through the setup process.</p>
        """,
        short_description="A modern wireless file transfer application for seamless sharing between devices.",
        has_download=True,
    )
    
    # You would need to add actual files in a real implementation
    # wifile.thumbnail.save('wifile.jpg', ImageFile(open('path_to_thumbnail', 'rb')))
    # wifile.download_file.save('wifile.zip', File(open('path_to_zip', 'rb')))
    wifile.save()
    
    # Create Caluu project
    caluu = Project(
        title="Caluu",
        slug="caluu",
        description="""
        <h3>Caluu - Advanced Calculator Web Application</h3>
        <p>Caluu is a comprehensive web-based calculator application that goes beyond basic arithmetic to provide advanced mathematical functions, unit conversions, and formula references.</p>
        
        <h4>Key Features:</h4>
        <ul>
            <li>Scientific calculator with advanced functions</li>
            <li>Graphing capabilities for functions and equations</li>
            <li>Unit conversion tools for various measurement systems</li>
            <li>Formula reference library for mathematics, physics, and chemistry</li>
            <li>History tracking for all calculations</li>
            <li>Ability to save and share calculation sets</li>
        </ul>
        
        <p>Visit the Caluu website to start using this powerful tool for all your calculation needs!</p>
        """,
        short_description="An advanced web-based calculator application with scientific and graphing features.",
        external_url="https://caluu.pythonanywhere.com",
    )
    
    # caluu.thumbnail.save('caluu.jpg', ImageFile(open('path_to_thumbnail', 'rb')))
    caluu.save()
    
    print("Projects initialized successfully!")

# To run this script:
# python manage.py runscript initialize_projects