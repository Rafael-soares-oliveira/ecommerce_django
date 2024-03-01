from django.contrib import admin
from .models import UserProfile


class UserProfileAdmin(admin.ModelAdmin):
    model = UserProfile


admin.site.register(UserProfile)
