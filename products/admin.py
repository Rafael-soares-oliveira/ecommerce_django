from django.contrib import admin
from .models import Product, ProductVariation


@admin.register(Product)
class ProductSiteAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        "slug": ('product_name',)
    }
    list_display = ['id', 'product_name']
    list_display_links = ['product_name']
    ordering = ['-id']
    list_per_page = 30
    search_fields = ['product_name']


@admin.register(ProductVariation)
class ProductStockAdmin(admin.ModelAdmin):
    ...
