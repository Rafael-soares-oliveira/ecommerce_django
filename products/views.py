from django.views.generic import ListView, DetailView, View
from products.models import Product, ProductVariation
import os

PER_PAGE = os.environ.get('PER_PAGE', 6)


class ProductsViewBase(ListView):
    model = ProductVariation
    context_object_name = 'products'
    ordering = ['-id']


class ProductsViewHome(ProductsViewBase):
    template_name = 'pages/home.html'


class ProductDetail(DetailView):
    model = Product
    context_object_name = 'product_'
    template_name = 'pages/product_detail.html'


class AddCart(ProductsViewBase):
    template_name = 'pages/cart.html'


class RemoveCart(View):
    pass


class Cart(View):
    pass


class End(View):
    pass
