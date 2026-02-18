from django.urls import path
from .views import page_detail

app_name = 'page_builder'

urlpatterns = [
    path('<slug:slug>/', page_detail, name='page_detail'),
]
