from django.shortcuts import render, get_object_or_404
from blog.models.category import Category
from blog.models.tag import Tag
from blog.services.post_service import PostService
from blog.services.category_service import CategoryService

def category_list(request, slug):
    category = get_object_or_404(Category, slug=slug)
    posts_list = category.posts.filter(status='published').order_by('-published_at')
    posts = PostService.get_paginated_posts(posts_list, request.GET.get('page'))
    return render(request, 'blog/category_posts.html', {'category': category, 'posts': posts})

def category_list_all(request):
    categories = CategoryService.get_active_categories()
    return render(request, 'blog/all_categories.html', {'categories': categories})

def tag_list(request, slug):
    tag = get_object_or_404(Tag, slug=slug)
    posts_list = tag.posts.filter(status='published').order_by('-published_at')
    posts = PostService.get_paginated_posts(posts_list, request.GET.get('page'))
    return render(request, 'blog/tag_list.html', {'tag': tag, 'posts': posts})
