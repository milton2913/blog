from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

class Menu(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    
    def __str__(self):
        return self.name

class MenuItem(models.Model):
    LINK_TYPES = (
        ('manual', 'Manual URL'),
        ('object', 'Internal Content (Post, Category, Tag, Page)'),
    )
    
    menu = models.ForeignKey(Menu, related_name='items', on_delete=models.CASCADE)
    title = models.CharField(max_length=100, help_text="Navigation text")
    link_type = models.CharField(max_length=10, choices=LINK_TYPES, default='manual')
    
    # For Manual URL
    url = models.CharField(max_length=255, blank=True, help_text="Used if link type is Manual")
    
    # For Internal Content (Generic Foreign Key)
    content_type = models.ForeignKey(
        ContentType, 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True,
        limit_choices_to={'model__in': ('post', 'category', 'tag', 'pages', 'page', 'theme')} # Dynamic filtering in admin is better
    )
    object_id = models.CharField(max_length=255, null=True, blank=True)
    content_object = GenericForeignKey('content_type', 'object_id')
    
    parent = models.ForeignKey('self', null=True, blank=True, related_name='children', on_delete=models.CASCADE)
    order = models.PositiveIntegerField(default=0)
    
    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title

    def get_url(self):
        if self.link_type == 'object' and self.content_object:
            try:
                return self.content_object.get_absolute_url()
            except AttributeError:
                # If no get_absolute_url, we might need manual mapping or handle it
                return "#"
        return self.url or "#"
