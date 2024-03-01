from django.views.generic import ListView
from products.models import Product


class ProductsViewBase(ListView):
    model = Product
    context_object_name = 'products'
    ordering = ['-id']


class ProductsViewHome(ProductsViewBase):
    template_name = "products/home.html"
