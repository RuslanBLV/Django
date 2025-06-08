from django.urls import path
from . import views

app_name = 'catalog'

urlpatterns = [
    path('home/', views.home_html, name='home_html'),
    path('contacts/', views.contacts_post, name='contacts_html'),
]