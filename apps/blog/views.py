from django.shortcuts import render, get_object_or_404
from django.db.models import Q, Count
from django.core.paginator import Paginator
from .models import Post, Category, Tag

def home(request):
    posts_list = Post.objects.filter(status='published').order_by('-published_at')
    paginator = Paginator(posts_list, 10) # Show 10 posts per page.
    page_number = request.GET.get('page')
    posts = paginator.get_page(page_number)
    return render(request, 'blog/home.html', {'posts': posts})

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug, status='published')
    related_posts = Post.objects.filter(tags__in=post.tags.all(), status='published').exclude(id=post.id).distinct()[:3]
    return render(request, 'blog/post_detail.html', {'post': post, 'related_posts': related_posts})

def category_list(request, slug):
    category = get_object_or_404(Category, slug=slug)
    posts_list = category.posts.filter(status='published').order_by('-published_at')
    paginator = Paginator(posts_list, 10)
    page_number = request.GET.get('page')
    posts = paginator.get_page(page_number)
    return render(request, 'blog/category_list.html', {'category': category, 'posts': posts})

def category_list_all(request):
    categories = Category.objects.filter(is_active=True).annotate(post_count=Count('posts', distinct=True))
    return render(request, 'blog/all_categories.html', {'categories': categories})

def tag_list(request, slug):
    tag = get_object_or_404(Tag, slug=slug)
    posts_list = tag.posts.filter(status='published').order_by('-published_at')
    paginator = Paginator(posts_list, 10)
    page_number = request.GET.get('page')
    posts = paginator.get_page(page_number)
    return render(request, 'blog/tag_list.html', {'tag': tag, 'posts': posts})

def search(request):
    query = request.GET.get('q')
    posts_list = Post.objects.filter(status='published')
    if query:
        posts_list = posts_list.filter(Q(title__icontains=query) | Q(content__icontains=query)).distinct()
    
    paginator = Paginator(posts_list, 10)
    page_number = request.GET.get('page')
    posts = paginator.get_page(page_number)
    
    return render(request, 'blog/search_results.html', {'posts': posts, 'query': query})

def about(request):
    return render(request, 'blog/about.html')

def privacy_policy(request):
    return render(request, 'blog/privacy_policy.html')

from .forms import ContactForm
from django.contrib import messages

def terms_conditions(request):
    return render(request, 'blog/terms_conditions.html')

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Send email logic here (placeholder)
            # send_mail(
            #     form.cleaned_data['subject'],
            #     form.cleaned_data['message'],
            #     form.cleaned_data['email'],
            #     ['admin@example.com'],
            #     fail_silently=False,
            # )
            messages.success(request, 'Your message has been sent successfully!')
            return render(request, 'blog/contact.html', {'form': ContactForm()})
    else:
        form = ContactForm()
    return render(request, 'blog/contact.html', {'form': form})
