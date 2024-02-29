from django.contrib import admin
from .models import Products


@admin.register(Products)
class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        "slug": ('product_name',)
    }
    list_display = ['id', 'product_name']
    list_display_links = ['product_name']
    ordering = ['-id']
    list_per_page = 30
    search_fields = ['product_name']
