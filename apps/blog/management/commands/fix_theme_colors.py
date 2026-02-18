from django.core.management.base import BaseCommand
from blog.models import ThemeSettings

class Command(BaseCommand):
    help = 'Fixes ThemeSettings color fields by ensuring they start with #'

    def handle(self, *args, **options):
        theme = ThemeSettings.objects.first()
        if theme:
            self.stdout.write(f'Original Primary Color: {theme.primary_color}')
            # The save method now has logic to add # if missing
            theme.save()
            self.stdout.write(self.style.SUCCESS(f'Fixed Primary Color: {theme.primary_color}'))
            self.stdout.write(self.style.SUCCESS('Theme settings updated successfully.'))
        else:
            self.stdout.write(self.style.WARNING('No ThemeSettings found.'))
