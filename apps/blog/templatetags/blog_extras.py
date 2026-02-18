from django import template
from blog.services.category_service import CategoryService, TagService
from blog.services.post_service import PostService

register = template.Library()

@register.inclusion_tag('blog/sidebar.html')
def show_sidebar():
    categories = CategoryService.get_active_categories().exclude(post_count=0)
    popular_tags = TagService.get_active_tags()[:10]  # TagService needs post count logic if wanted, for now just active
    recent_posts = PostService.get_published_posts()[:5]
    return {
        'categories': categories,
        'popular_tags': popular_tags,
        'recent_posts': recent_posts,
    }
