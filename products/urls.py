from django.urls import path
from products import views


app_name = 'products'

urlpatterns = [
    path('', views.ProductsViewHome.as_view(), name='home'),
    path('<slug>/', views.ProductDetail.as_view(), name='product_detail'),
    path('addcart/', views.AddCart.as_view(), name='add_cart'),
    path('removecart/', views.RemoveCart.as_view(), name='remove_cart'),
    path('cart/', views.Cart.as_view(), name='cart'),
    path('end/', views.End.as_view(), name='end'),
]
