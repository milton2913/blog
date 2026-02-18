from django.db import migrations


class Migration(migrations.Migration):
    """
    This migration moves the ThemeSettings table from the blog app to the
    settings app WITHOUT recreating the table or losing data.

    It uses SeparateDatabaseAndState to tell Django's ORM that the model
    is now in the 'settings' app, while the actual database table
    (blog_themesettings) is renamed to settings_themesettings.
    """

    dependencies = [
        ('blog', '0009_alter_comment_options_themesettings_email_active_and_more'),
    ]

    operations = [
        migrations.SeparateDatabaseAndState(
            database_operations=[
                migrations.RunSQL(
                    sql='ALTER TABLE blog_themesettings RENAME TO settings_themesettings;',
                    reverse_sql='ALTER TABLE settings_themesettings RENAME TO blog_themesettings;',
                ),
            ],
            state_operations=[
                migrations.CreateModel(
                    name='ThemeSettings',
                    fields=[
                        ('id', __import__('django.db.models', fromlist=['AutoField']).AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                        ('site_name', __import__('django.db.models', fromlist=['CharField']).CharField(default='Django Blog', max_length=100)),
                        ('primary_color', __import__('django.db.models', fromlist=['CharField']).CharField(default='#2B7DDD', help_text='Hex code (e.g. #2B7DDD)', max_length=7)),
                        ('background_color', __import__('django.db.models', fromlist=['CharField']).CharField(default='#F3F4F6', help_text='Hex code (e.g. #F3F4F6)', max_length=7)),
                        ('text_color', __import__('django.db.models', fromlist=['CharField']).CharField(default='#1F2937', help_text='Hex code (e.g. #1F2937)', max_length=7)),
                        ('link_color', __import__('django.db.models', fromlist=['CharField']).CharField(default='#2563EB', help_text='Hex code (e.g. #2563EB)', max_length=7)),
                        ('glass_opacity', __import__('django.db.models', fromlist=['DecimalField']).DecimalField(decimal_places=2, default=0.7, help_text='0.0 to 1.0', max_digits=3)),
                        ('glass_blur', __import__('django.db.models', fromlist=['IntegerField']).IntegerField(default=10, help_text='Blur amount in px')),
                        ('border_radius', __import__('django.db.models', fromlist=['CharField']).CharField(default='1rem', help_text='e.g. 1rem, 16px', max_length=10)),
                        ('site_description', __import__('django.db.models', fromlist=['TextField']).TextField(default='A modern Django blog.', help_text='Default meta description for the site.')),
                        ('site_keywords', __import__('django.db.models', fromlist=['CharField']).CharField(default='django, blog, python, web development', help_text='Comma-separated keywords.', max_length=255)),
                        ('twitter_handle', __import__('django.db.models', fromlist=['CharField']).CharField(blank=True, help_text='@yourhandle', max_length=100)),
                        ('facebook_app_id', __import__('django.db.models', fromlist=['CharField']).CharField(blank=True, help_text='Facebook App ID for Open Graph.', max_length=100)),
                        ('facebook_url', __import__('django.db.models', fromlist=['URLField']).URLField(blank=True, help_text='Facebook page URL')),
                        ('twitter_url', __import__('django.db.models', fromlist=['URLField']).URLField(blank=True, help_text='Twitter profile URL')),
                        ('instagram_url', __import__('django.db.models', fromlist=['URLField']).URLField(blank=True, help_text='Instagram profile URL')),
                        ('linkedin_url', __import__('django.db.models', fromlist=['URLField']).URLField(blank=True, help_text='LinkedIn profile URL')),
                        ('github_url', __import__('django.db.models', fromlist=['URLField']).URLField(blank=True, help_text='GitHub profile URL')),
                        ('email_active', __import__('django.db.models', fromlist=['BooleanField']).BooleanField(default=False, help_text='Enable custom SMTP settings')),
                        ('email_host', __import__('django.db.models', fromlist=['CharField']).CharField(blank=True, help_text='SMTP Host (e.g., smtp.gmail.com)', max_length=255)),
                        ('email_port', __import__('django.db.models', fromlist=['IntegerField']).IntegerField(default=587, help_text='SMTP Port (e.g., 587)')),
                        ('email_host_user', __import__('django.db.models', fromlist=['CharField']).CharField(blank=True, help_text='SMTP Username', max_length=255)),
                        ('email_host_password', __import__('django.db.models', fromlist=['CharField']).CharField(blank=True, help_text='SMTP Password', max_length=255)),
                        ('email_use_tls', __import__('django.db.models', fromlist=['BooleanField']).BooleanField(default=True, help_text='Use TLS')),
                        ('email_use_ssl', __import__('django.db.models', fromlist=['BooleanField']).BooleanField(default=False, help_text='Use SSL')),
                        ('email_from_email', __import__('django.db.models', fromlist=['EmailField']).EmailField(blank=True, help_text="Default 'From' email address", max_length=254)),
                    ],
                    options={
                        'verbose_name': 'Theme Settings',
                        'verbose_name_plural': 'Theme Settings',
                    },
                ),
            ],
        ),
    ]
