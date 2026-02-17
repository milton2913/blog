from django import template
from django.db.models import Count
from blog.models import Category, Tag, Post

register = template.Library()

@register.inclusion_tag('blog/sidebar.html')
def show_sidebar():
    categories = Category.objects.filter(is_active=True).annotate(post_count=Count('posts', distinct=True)).exclude(post_count=0)
    popular_tags = Tag.objects.filter(is_active=True).annotate(post_count=Count('posts', distinct=True)).order_by('-post_count')[:10]
    recent_posts = Post.objects.filter(status='published').order_by('-published_at')[:5]
    return {
        'categories': categories,
        'popular_tags': popular_tags,
        'recent_posts': recent_posts,
    }
