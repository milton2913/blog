from django.contrib import admin
from .models import Menu, MenuItem

class MenuItemInline(admin.TabularInline):
    model = MenuItem
    extra = 1
    fields = ('title', 'link_type', 'url', 'content_type', 'object_id', 'parent', 'order')
    sortable_field_name = "order"

@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}
    inlines = [MenuItemInline]

@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'menu', 'link_type', 'parent', 'order')
    list_filter = ('menu', 'link_type')
    search_fields = ('title', 'url')
