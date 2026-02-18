from django.shortcuts import render, get_object_or_404
from .models import Page

def page_detail(request, slug):
    page = get_object_or_404(Page, slug=slug, status='published')
    blocks = page.blocks.all()
    return render(request, 'page_builder/page_detail.html', {
        'page': page,
        'blocks': blocks
    })
