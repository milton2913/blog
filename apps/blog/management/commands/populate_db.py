import random
from django.core.management.base import BaseCommand
from django.utils.text import slugify
from blog.models import Category, Tag, Post
from django.contrib.auth import get_user_model
from django.utils import timezone

User = get_user_model()

class Command(BaseCommand):
    help = 'Populate database with fake data'

    def handle(self, *args, **kwargs):
        self.stdout.write('Populating database...')

        # Ensure we have a user
        user = User.objects.first()
        if not user:
            self.stdout.write(self.style.ERROR('No user found. Please create a superuser first.'))
            return

        # Categories
        categories = [
            'Technology', 'Travel', 'Food', 'Lifestyle', 'Health',
            'Business', 'Education', 'Entertainment', 'Science', 'Sports'
        ]
        
        cat_objs = []
        for cat_name in categories:
            cat, created = Category.objects.get_or_create(name=cat_name, defaults={'description': f'All about {cat_name}'})
            cat_objs.append(cat)
            self.stdout.write(f'Category: {cat.name}')

        # Tags
        tags_list = [
            'Django', 'Python', 'Web Development', 'Tutorial', 'coding',
            'Travel Tips', 'Holiday', 'Recipes', 'Healthy', 'Fitness',
            'Startup', 'Marketing', 'Learning', 'Movies', 'Music',
            'Physics', 'Space', 'Football', 'Cricket', 'Tennis'
        ]
        
        tag_objs = []
        for tag_name in tags_list:
            tag, created = Tag.objects.get_or_create(name=tag_name)
            tag_objs.append(tag)
            self.stdout.write(f'Tag: {tag.name}')

        # Posts
        for i in range(50):
            title = f'Blog Post Title {i+1}'
            content = f'This is the content for blog post {i+1}. ' * 20
            category = random.choice(cat_objs)
            
            post, created = Post.objects.get_or_create(
                title=title,
                defaults={
                    'content': content,
                    'category': category,
                    'author': user,
                    'status': 'published' if i % 5 != 0 else 'draft', # Mostly published
                    'published_at': timezone.now() if i % 5 != 0 else None,
                }
            )
            
            # Assign random tags
            post_tags = random.sample(tag_objs, k=random.randint(1, 4))
            post.tags.set(post_tags)
            
            self.stdout.write(f'Post: {post.title} ({post.status})')

        self.stdout.write(self.style.SUCCESS('Database populated successfully!'))
