from django.urls import path
from ..views.static_views import about, privacy_policy, terms_conditions
from ..views.contact_views import contact

urlpatterns = [
    path('about/', about, name='about'),
    path('privacy-policy/', privacy_policy, name='privacy_policy'),
    path('terms-conditions/', terms_conditions, name='terms_conditions'),
    path('contact/', contact, name='contact'),
]
