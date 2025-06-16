from django.urls import path
from . import views

app_name = 'catalog'

urlpatterns = [
    path('home/', views.home_html, name='home_html'),
    path('contacts/', views.contacts_post, name='contacts_html'),
    path('index/', views.index, name='index'),
    path('product_detail/<int:product_id>/', views.product_detail, name='product_detail'),
    path('product_list/', views.product_list, name='product_list'),
]

