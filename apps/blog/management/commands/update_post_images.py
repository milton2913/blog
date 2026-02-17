from django.core.management.base import BaseCommand
from django.core.files import File
from django.conf import settings
from blog.models import Post
import requests
import tempfile
import random
import os

class Command(BaseCommand):
    help = 'Updates featured_image for all posts with random images from Picsum'

    def handle(self, *args, **options):
        posts = Post.objects.all()
        count = posts.count()
        self.stdout.write(f'Found {count} posts to update...')

        # Ensure media directory exists
        media_root = settings.MEDIA_ROOT
        posts_dir = os.path.join(media_root, 'posts')
        os.makedirs(posts_dir, exist_ok=True)

        for i, post in enumerate(posts):
            try:
                # Use a specific seed to get a deterministic random image for debugging, 
                # or just random seed for variety. Using post.id as seed ensures consistent image per post if re-run.
                # But here we want variety, so let's use random.
                seed = random.randint(1, 100000)
                image_url = f'https://picsum.photos/seed/{seed}/800/600'
                
                response = requests.get(image_url, stream=True)
                
                if response.status_code == 200:
                    # Create a temporary file
                    img_temp = tempfile.NamedTemporaryFile(delete=True)
                    img_temp.write(response.content)
                    img_temp.flush()

                    file_name = f'post_{post.id}_image.jpg'
                    
                    # Save the image to the model field
                    post.featured_image.save(file_name, File(img_temp), save=True)
                    
                    self.stdout.write(self.style.SUCCESS(f'[{i+1}/{count}] Updated image for post "{post.title}"'))
                else:
                    self.stdout.write(self.style.WARNING(f'Failed to download image for post "{post.title}" (Status: {response.status_code})'))

            except Exception as e:
                self.stdout.write(self.style.ERROR(f'Error updating post "{post.title}": {str(e)}'))

        self.stdout.write(self.style.SUCCESS('Successfully updated all post images!'))
