from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    class Role(models.TextChoices):
        ADMIN = 'ADMIN', 'Admin'
        EDITOR = 'EDITOR', 'Editor'
        USER = 'USER', 'User'

    role = models.CharField(max_length=50, choices=Role.choices, default=Role.USER)
    profile_image = models.ImageField(upload_to='profiles/', blank=True, null=True)
    
    # Social Media Links
    bio = models.TextField(blank=True, help_text="Short bio for author profile")
    facebook_url = models.URLField(blank=True, help_text="Facebook profile URL")
    twitter_url = models.URLField(blank=True, help_text="Twitter profile URL")
    instagram_url = models.URLField(blank=True, help_text="Instagram profile URL")
    linkedin_url = models.URLField(blank=True, help_text="LinkedIn profile URL")
    github_url = models.URLField(blank=True, help_text="GitHub profile URL")

    def __str__(self):
        return self.username
