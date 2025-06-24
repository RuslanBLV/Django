from django.contrib import admin
from .models import Blog


@admin.register(Blog)
class Blogadmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description',)
    search_fields = ('title', 'title',)
