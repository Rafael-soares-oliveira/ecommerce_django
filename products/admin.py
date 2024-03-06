from django.contrib import admin
from .models import Product, ProductVariation


class ProductVariationAdmin(admin.TabularInline):
    model = ProductVariation
    extra = 1
    prepopulated_fields = {
        "slug": ('variation_name',),
    }


class ProductAdmin(admin.ModelAdmin):
    model = Product
    prepopulated_fields = {
        "slug": ('product_name',),
    }
    list_display = ['product_name', 'short_description', 'get_price',
                    'get_offer_price']
    list_display_links = ['product_name']
    ordering = ['-id']
    list_per_page = 30
    search_fields = ['product_name']
    inlines = [
        ProductVariationAdmin
    ]


admin.site.register(Product, ProductAdmin)
