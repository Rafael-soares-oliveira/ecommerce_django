from django.urls import path
from orders import views

app_name = 'orders'

urlpatterns = [
    path('payment/', views.Payment.as_view(), name='payment'),
    path('finish_order/', views.FinishOrder.as_view(), name='finish_order'),
    path('order_detail/<int:pk>/', views.OrderDetail.as_view(),
         name='order_detail'),
]
