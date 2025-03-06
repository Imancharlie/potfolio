# Generated by Django 5.1.6 on 2025-03-06 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Project",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=100)),
                ("slug", models.SlugField(unique=True)),
                ("description", models.TextField()),
                ("short_description", models.CharField(max_length=200)),
                ("thumbnail", models.ImageField(upload_to="project_thumbnails/")),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("has_download", models.BooleanField(default=False)),
                (
                    "download_file",
                    models.FileField(blank=True, null=True, upload_to="downloads/"),
                ),
                ("external_url", models.URLField(blank=True, null=True)),
            ],
        ),
    ]
