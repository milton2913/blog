from django.db import models
from django.utils.text import slugify
from django.conf import settings
from django.contrib.auth import get_user_model

User = get_user_model()

class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True, blank=True) # editable=True by default
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    feature_image = models.ImageField(upload_to='categories/', blank=True, null=True)
    icon = models.CharField(max_length=50, blank=True, help_text="FontAwesome class (e.g., 'fas fa-code')")
    
    # SEO Fields
    meta_title = models.CharField(max_length=200, blank=True, help_text="SEO Title. Defaults to Name.")
    meta_description = models.TextField(blank=True, help_text="SEO Description. Defaults to Description.")
    meta_keywords = models.CharField(max_length=255, blank=True, help_text="Comma-separated keywords.")

    class Meta:
        verbose_name_plural = 'Categories'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True, blank=True)
    is_active = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )

    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    content = models.TextField()
    featured_image = models.ImageField(upload_to='posts/', blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='posts')
    tags = models.ManyToManyField(Tag, related_name='posts', blank=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='posts')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    published_at = models.DateTimeField(blank=True, null=True)
    is_active = models.BooleanField(default=True)

    # SEO Fields
    meta_title = models.CharField(max_length=200, blank=True, help_text="SEO Title. Defaults to Title.")
    meta_description = models.TextField(blank=True, help_text="SEO Description. Defaults to truncated content.")
    meta_keywords = models.CharField(max_length=255, blank=True, help_text="Comma-separated keywords.")
    
    # pgvector field can be added later as per requirement

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

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

    def __str__(self):
        return "Theme Settings"

    class Meta:
        verbose_name = "Theme Settings"
        verbose_name_plural = "Theme Settings"

    def save(self, *args, **kwargs):
        if not self.pk and ThemeSettings.objects.exists():
            # If you want to ensure only one instance, enabling this check prevents creating more.
            # But for simplicity in admin, we can just grab the first one.
            pass
        super().save(*args, **kwargs)
