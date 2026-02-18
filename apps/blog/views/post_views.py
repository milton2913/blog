from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from blog.models.post import Post
from blog.forms import CommentForm
from blog.services.post_service import PostService
from blog.services.comment_service import CommentService

def home(request):
    posts_list = PostService.get_published_posts()
    posts = PostService.get_paginated_posts(posts_list, request.GET.get('page'))
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug, status='published')
    
    if request.method == 'POST':
        comment, form = CommentService.handle_comment_submission(post, request.POST, request.user)
        if comment:
            if request.POST.get('ajax') == '1':
                comments = CommentService.get_active_root_comments(post)
                return render(request, 'blog/comments.html', {'comments': comments, 'post': post})
            messages.success(request, 'Your comment has been submitted!')
            return redirect('blog:post_detail', slug=post.slug)
    else:
        initial_data = {}
        if request.user.is_authenticated:
            initial_data = {
                'name': request.user.get_full_name() or request.user.username,
                'email': request.user.email
            }
        form = CommentForm(initial=initial_data)

    comments = CommentService.get_active_root_comments(post)
    related_posts = Post.objects.filter(tags__in=post.tags.all(), status='published').exclude(id=post.id).distinct()[:3]
    
    return render(request, 'blog/post_detail.html', {
        'post': post,
        'comments': comments,
        'comment_form': form,
        'related_posts': related_posts
    })

def search(request):
    query = request.GET.get('q')
    posts_list = PostService.search_posts(query)
    posts = PostService.get_paginated_posts(posts_list, request.GET.get('page'))
    return render(request, 'blog/search_results.html', {'posts': posts, 'query': query})
