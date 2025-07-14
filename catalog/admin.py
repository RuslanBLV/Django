from django.contrib import admin
from .models import Category, Product


@admin.register(Product)
class Productadmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'category_product')
    list_filter = ('category_product',)
    search_fields = ('name', 'name',)


@admin.register(Category)
class Categoryadmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
