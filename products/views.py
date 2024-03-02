from django.utils import translation
from django.http import Http404
from django.views.generic import ListView, DetailView, View
from products.models import Product
from utils.pagination import make_pagination
import os

PER_PAGE = os.environ.get('PER_PAGE', 6)


class ProductsViewBase(ListView):
    model = Product
    context_object_name = 'products'
    ordering = ['-id']

    def get_queryset(self, *args, **kwargs):
        qs = super().get_queryset(*args, **kwargs)
        return qs

    def get_context_data(self, *args, **kwargs):
        ctx = super().get_context_data(*args, **kwargs)
        page_obj, pagination_range = make_pagination(
            self.request,
            ctx.get('products'),
            PER_PAGE
        )
        html_language = translation.get_language()
        ctx.update({
            'products': page_obj,
            'pagination_range': pagination_range,
            'last_page': pagination_range['total_pages'],
            'html_language': html_language,
        })
        return ctx


class ProductsViewHome(ProductsViewBase):
    template_name = 'pages/home.html'


class ProductDetail(DetailView):
    model = Product
    context_object_name = 'product'
    template_name = 'pages/product_detail.html'

    def get_queryset(self, *args, **kwargs):
        qs = super().get_queryset(*args, **kwargs)
        if not qs:
            raise Http404
        return qs

    def get_context_data(self, *args, **kwargs):
        ctx = super().get_context_data(*args, **kwargs)
        ctx.update({
            'is_detail_page': True,
        })
        return ctx


class AddCart(ProductsViewBase):
    template_name = 'pages/cart.html'


class RemoveCart(View):
    pass


class Cart(View):
    pass


class End(View):
    pass
