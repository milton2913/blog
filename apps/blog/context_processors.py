from .models import ThemeSettings

def theme_settings(request):
    try:
        theme = ThemeSettings.objects.first()
        if not theme:
            # Return defaults if no settings exist
            return {
                'theme': {
                    'site_name': 'Django Blog',
                    'primary_color': '#2B7DDD',
                    'background_color': '#F3F4F6',
                    'text_color': '#1F2937',
                    'link_color': '#2563EB',
                    'glass_opacity': 0.70,
                    'glass_blur': 10,
                    'border_radius': '1rem',
                    'site_description': 'A modern Django blog.',
                    'site_keywords': 'django, blog, python',
                    'twitter_handle': '',
                    'facebook_app_id': '',
                }
            }
        return {'theme': theme}
    except:
        return {}
