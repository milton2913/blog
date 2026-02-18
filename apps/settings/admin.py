from django.contrib import admin
from .models import ThemeSettings


@admin.register(ThemeSettings)
class ThemeSettingsAdmin(admin.ModelAdmin):
    list_display = ('site_name', 'primary_color', 'glass_opacity')
    change_form_template = 'admin/settings/themesettings/change_form.html'

    fieldsets = (
        ('General Settings', {
            'fields': ('site_name', 'primary_color', 'background_color', 'text_color', 'link_color')
        }),
        ('Glassmorphism', {
            'fields': ('glass_opacity', 'glass_blur', 'border_radius')
        }),
        ('SEO Settings', {
            'fields': ('site_description', 'site_keywords', 'twitter_handle', 'facebook_app_id'),
        }),
        ('Social Media Links', {
            'fields': ('facebook_url', 'twitter_url', 'instagram_url', 'linkedin_url', 'github_url'),
        }),
        ('SMTP Settings', {
            'fields': (
                'email_active', 'email_host', 'email_port',
                'email_host_user', 'email_host_password',
                'email_use_tls', 'email_use_ssl', 'email_from_email'
            ),
            'description': 'Configure your email provider settings here. (e.g., Gmail, Outlook, etc.)'
        }),
    )

    def has_add_permission(self, request):
        return not ThemeSettings.objects.exists()

    def has_delete_permission(self, request, obj=None):
        return False
