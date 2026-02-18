from django.db import models


class ThemeSettings(models.Model):
    site_name = models.CharField(max_length=100, default="Django Blog")
    primary_color = models.CharField(max_length=7, default="#2B7DDD", help_text="Hex code (e.g. #2B7DDD)")
    background_color = models.CharField(max_length=7, default="#F3F4F6", help_text="Hex code (e.g. #F3F4F6)")
    text_color = models.CharField(max_length=7, default="#1F2937", help_text="Hex code (e.g. #1F2937)")
    link_color = models.CharField(max_length=7, default="#2563EB", help_text="Hex code (e.g. #2563EB)")
    glass_opacity = models.DecimalField(max_digits=3, decimal_places=2, default=0.70, help_text="0.0 to 1.0")
    glass_blur = models.IntegerField(default=10, help_text="Blur amount in px")
    border_radius = models.CharField(max_length=10, default="1rem", help_text="e.g. 1rem, 16px")

    # SEO - Global Defaults
    site_description = models.TextField(default="A modern Django blog.", help_text="Default meta description for the site.")
    site_keywords = models.CharField(max_length=255, default="django, blog, python, web development", help_text="Comma-separated keywords.")
    twitter_handle = models.CharField(max_length=100, blank=True, help_text="@yourhandle")
    facebook_app_id = models.CharField(max_length=100, blank=True, help_text="Facebook App ID for Open Graph.")

    # Social Media Links - System Wide
    facebook_url = models.URLField(blank=True, help_text="Facebook page URL")
    twitter_url = models.URLField(blank=True, help_text="Twitter profile URL")
    instagram_url = models.URLField(blank=True, help_text="Instagram profile URL")
    linkedin_url = models.URLField(blank=True, help_text="LinkedIn profile URL")
    github_url = models.URLField(blank=True, help_text="GitHub profile URL")

    # SMTP Settings (Dynamic Email Configuration)
    email_active = models.BooleanField(default=False, help_text="Enable custom SMTP settings")
    email_host = models.CharField(max_length=255, blank=True, help_text="SMTP Host (e.g., smtp.gmail.com)")
    email_port = models.IntegerField(default=587, help_text="SMTP Port (e.g., 587)")
    email_host_user = models.CharField(max_length=255, blank=True, help_text="SMTP Username")
    email_host_password = models.CharField(max_length=255, blank=True, help_text="SMTP Password")
    email_use_tls = models.BooleanField(default=True, help_text="Use TLS")
    email_use_ssl = models.BooleanField(default=False, help_text="Use SSL")
    email_from_email = models.EmailField(blank=True, help_text="Default 'From' email address")

    def __str__(self):
        return "Theme Settings"

    class Meta:
        verbose_name = "Theme Settings"
        verbose_name_plural = "Theme Settings"

    def save(self, *args, **kwargs):
        # Ensure colors start with #
        color_fields = ['primary_color', 'background_color', 'text_color', 'link_color']
        for field in color_fields:
            value = getattr(self, field)
            if value and not value.startswith('#'):
                setattr(self, field, f'#{value}')
        super().save(*args, **kwargs)
