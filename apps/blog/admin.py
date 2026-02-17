from django.contrib import admin
from .models import Category, Tag, Post, Comment

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'is_active', 'created_at', 'icon')
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}
    list_filter = ('is_active',)
    fieldsets = (
        (None, {
            'fields': ('name', 'slug', 'description', 'feature_image', 'icon', 'is_active')
        }),
        ('SEO', {
            'fields': ('meta_title', 'meta_description', 'meta_keywords'),
            'classes': ('collapse',)
        }),
    )

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'is_active')
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}
    list_filter = ('is_active',)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'status', 'created_at', 'is_active')
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('status', 'created_at', 'category', 'tags', 'is_active')
    autocomplete_fields = ['category', 'tags', 'author']
    fieldsets = (
        (None, {
            'fields': ('title', 'slug', 'content', 'featured_image')
        }),
        ('Metadata', {
            'fields': ('author', 'category', 'tags', 'status', 'published_at', 'is_active')
        }),
        ('SEO', {
            'fields': ('meta_title', 'meta_description', 'meta_keywords'),
            'classes': ('collapse',)
        }),
    )

from .models import ThemeSettings

@admin.register(ThemeSettings)
class ThemeSettingsAdmin(admin.ModelAdmin):
    list_display = ('site_name', 'primary_color', 'glass_opacity')
    fieldsets = (
        ('General Settings', {
            'fields': ('site_name', 'primary_color', 'background_color', 'text_color', 'link_color')
        }),
        ('Glassmorphism', {
            'fields': ('glass_opacity', 'glass_blur', 'border_radius')
        }),
        ('SEO Settings', {
            'fields': ('site_description', 'site_keywords', 'twitter_handle', 'facebook_app_id'),
            'classes': ('collapse',)
        }),
        ('Social Media Links', {
            'fields': ('facebook_url', 'twitter_url', 'instagram_url', 'linkedin_url', 'github_url'),
            'classes': ('collapse',)
        }),
    )
    
    def has_add_permission(self, request):
        # Only allow one instance
        if self.model.objects.exists():
            return False
        return super().has_add_permission(request)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'post', 'created_at', 'active')
    list_filter = ('active', 'created_at')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)

