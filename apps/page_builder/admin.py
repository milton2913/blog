from django.contrib import admin
from .models import Page, PageBlock

class PageBlockInline(admin.StackedInline):
    model = PageBlock
    extra = 1
    sortable_field_name = "order"

@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status', 'created_at')
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('status', 'created_at')
    search_fields = ('title', 'slug', 'meta_description')
    
    fieldsets = (
        (None, {
            'fields': ('title', 'slug', 'status')
        }),
        ('SEO Settings', {
            'classes': ('collapse',),
            'fields': ('meta_title', 'meta_description'),
        }),
    )
    inlines = [PageBlockInline]

@admin.register(PageBlock)
class PageBlockAdmin(admin.ModelAdmin):
    list_display = ('block_type', 'page', 'order')
    list_filter = ('block_type', 'page')
