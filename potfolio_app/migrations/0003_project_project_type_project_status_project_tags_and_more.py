# Generated by Django 5.1.6 on 2025-03-09 17:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("potfolio_app", "0002_feedback"),
    ]

    operations = [
        migrations.AddField(
            model_name="project",
            name="project_type",
            field=models.CharField(
                choices=[
                    ("web", "Web App"),
                    ("desktop", "Desktop App"),
                    ("mobile", "Mobile App"),
                    ("other", "Other"),
                ],
                default="web",
                max_length=50,
            ),
        ),
        migrations.AddField(
            model_name="project",
            name="status",
            field=models.CharField(
                choices=[
                    ("completed", "Completed"),
                    ("in_progress", "In Progress"),
                    ("planned", "Planned"),
                ],
                default="completed",
                max_length=20,
            ),
        ),
        migrations.AddField(
            model_name="project",
            name="tags",
            field=models.CharField(
                blank=True,
                help_text="Comma-separated tags, e.g., 'File Transfer, Desktop'",
                max_length=200,
            ),
        ),
        migrations.AddField(
            model_name="project",
            name="technologies",
            field=models.CharField(
                blank=True,
                help_text="Comma-separated tech stack, e.g., 'Django, JavaScript'",
                max_length=200,
            ),
        ),
        migrations.AddField(
            model_name="project",
            name="version",
            field=models.CharField(default="1.0", max_length=10),
        ),
        migrations.CreateModel(
            name="ProjectMedia",
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
                (
                    "image",
                    models.ImageField(
                        blank=True, null=True, upload_to="project_media/"
                    ),
                ),
                ("caption", models.CharField(blank=True, max_length=100)),
                ("order", models.PositiveIntegerField(default=0)),
                (
                    "project",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="media",
                        to="potfolio_app.project",
                    ),
                ),
            ],
            options={
                "ordering": ["order"],
            },
        ),
    ]
