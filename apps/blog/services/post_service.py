from django.db.models import Q
from django.core.paginator import Paginator
from blog.models.post import Post

class PostService:
    @staticmethod
    def get_published_posts():
        return Post.objects.filter(status='published').order_by('-published_at')

    @staticmethod
    def get_paginated_posts(posts_list, page_number, per_page=10):
        paginator = Paginator(posts_list, per_page)
        return paginator.get_page(page_number)

    @staticmethod
    def search_posts(query):
        posts_list = Post.objects.filter(status='published')
        if query:
            posts_list = posts_list.filter(
                Q(title__icontains=query) | Q(content__icontains=query)
            ).distinct()
        return posts_list
