from django.urls import path
from . import views

app_name = 'catalog'

urlpatterns = [
    path('home_html/', views.home_html, name='home_html'),
    path('contacts_post/', views.contacts_post, name='contacts_post'),
]