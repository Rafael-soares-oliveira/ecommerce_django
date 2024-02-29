from django.views.generic import ListView
from products.models import Products


class ProductsViewBase(ListView):
    model = Products
    context_object_name = 'products'
    ordering = ['-id']


class ProductsViewHome(ProductsViewBase):
    template_name = "products/home.html"
