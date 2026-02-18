from django.db import models
from django.utils.text import slugify
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True, blank=True)
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
        app_label = 'blog'
        verbose_name_plural = 'Categories'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('blog:category_list', kwargs={'slug': self.slug})
