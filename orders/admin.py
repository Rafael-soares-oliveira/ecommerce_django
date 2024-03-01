from django.contrib import admin
from .models import Order, OrderItem


class OrderItemAdmin(admin.TabularInline):
    model = OrderItem
    extra = 1


class OrderAdmin(admin.ModelAdmin):
    inlines = [
        OrderItemAdmin
    ]


admin.site.register(Order, OrderAdmin)
