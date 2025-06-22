from django.urls import path
from . import views

app_name = 'catalog'

urlpatterns = [
    path('home/', views.home_html, name='home_html'),
    path('product/contacts/', views.ContactsView.as_view(), name='contacts_html'),
    # path('index/', views.index, name='index'),
    # path('product_detail/<int:product_id>/', views.product_detail, name='product_detail'),
    # path('', views., name='product_list'),
    path('product/detail/<int:pk>/', views.ProductDetailView.as_view(), name='product_detail'),
    path('product/list/', views.ProductListView.as_view(), name='product_list'),
    path('product/create/', views.ProductCreateView.as_view(), name='product_create'),
    path('product/update/<int:pk>/', views.ProductUpdateView.as_view(), name='product_update'),
    path('product/delete/<int:pk>/', views.ProductDeleteView.as_view(), name='product_delete'),
]

