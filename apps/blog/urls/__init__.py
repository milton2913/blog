from django.urls import path, include

app_name = 'blog'

urlpatterns = [
    path('', include('apps.blog.urls.post_urls')),
]
