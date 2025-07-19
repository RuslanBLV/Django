from django.contrib import admin
from .models import CustomUser


@admin.register(CustomUser)
class Useradmin(admin.ModelAdmin):
    exclude = ('password', )
