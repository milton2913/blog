from django.db import models
from django.urls import reverse

class Page(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    
    # SEO
    meta_title = models.CharField(max_length=200, blank=True)
    meta_description = models.TextField(blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('page_builder:page_detail', kwargs={'slug': self.slug})

class PageBlock(models.Model):
    BLOCK_TYPES = (
        ('hero', 'Hero Section'),
        ('text', 'Rich Text'),
        ('image_text', 'Image with Text'),
        ('featured_posts', 'Featured Posts Grid'),
        ('cta', 'Call to Action'),
        ('html', 'Custom HTML'),
    )
    
    page = models.ForeignKey(Page, related_name='blocks', on_delete=models.CASCADE)
    block_type = models.CharField(max_length=20, choices=BLOCK_TYPES)
    
    # Store settings/content as JSON for flexibility
    # E.g. {"headline": "Hello", "subheadline": "World", "button_text": "Click", "button_url": "/"}
    data = models.JSONField(default=dict, blank=True)
    
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.get_block_type_display()} on {self.page.title}"
