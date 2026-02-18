from django.urls import path
from ..views.post_views import home, post_detail, search
from ..views.category_views import category_list, category_list_all, tag_list

urlpatterns = [
    path('', home, name='home'),
    path('post/<slug:slug>/', post_detail, name='post_detail'),
    path('search/', search, name='search'),
    path('categories/', category_list_all, name='category_list_all'),
    path('category/<slug:slug>/', category_list, name='category_list'),
    path('tag/<slug:slug>/', tag_list, name='tag_list'),
]
