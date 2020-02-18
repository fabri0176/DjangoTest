from django.urls import path
from .views import news, home, contact

urlpatterns = [
    path('', home, name='home'),
    path('news/', news, name='news'),
    path('contact/', news, name='contact'),
]