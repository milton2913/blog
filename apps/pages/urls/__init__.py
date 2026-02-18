from django.urls import path, include

app_name = 'pages'

urlpatterns = [
    path('', include('apps.pages.urls.page_urls')),
]
