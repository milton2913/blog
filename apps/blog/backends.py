from django.core.mail.backends.smtp import EmailBackend
from django.conf import settings
from .models import ThemeSettings

class DynamicSMTPEmailBackend(EmailBackend):
    def __init__(self, fail_silently=False, **kwargs):
        super().__init__(fail_silently=fail_silently)
        self.configure_settings()

    def configure_settings(self):
        try:
            theme_settings = ThemeSettings.objects.first()
            if theme_settings and theme_settings.email_active:
                self.host = theme_settings.email_host
                self.port = theme_settings.email_port
                self.username = theme_settings.email_host_user
                self.password = theme_settings.email_host_password
                self.use_tls = theme_settings.email_use_tls
                self.use_ssl = theme_settings.email_use_ssl
                # We can't easily override DEFAULT_FROM_EMAIL dynamically for everything without restart,
                # but we can set it for specific messages if needed. 
                # For the backend connection itself, these are the key params.
            else:
                # Fallback to Django settings
                pass 
        except Exception:
            # Fallback if DB is not ready
            pass
