from django.views.generic import ListView, DetailView, View
from products.models import Product
import os

PER_PAGE = os.environ.get('PER_PAGE', 6)


class ProductsViewBase(ListView):
    model = Product
    context_object_name = 'products'
    ordering = ['-id']
    paginate_by = 6


class ProductsViewHome(ProductsViewBase):
    template_name = 'pages/home.html'


class ProductDetail(DetailView):
    model = Product
    context_object_name = 'products'
    template_name = 'pages/product_detail.html'
    slug_url_kwarg = 'slug'

    def get_context_data(self, *args, **kwargs):
        ctx = super().get_context_data(*args, **kwargs)
        product = Product.objects.get(
            slug=self.kwargs.get('slug', ''))
        variations = product.variations.all()  # type: ignore
        ctx.update({
            'variations': variations,
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
