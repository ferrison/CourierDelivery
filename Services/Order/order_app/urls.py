from django.urls import path

from order_app import views

urlpatterns = [
    path('order/<uuid:id>', views.OrderDetailView.as_view(), name='order_detail'),
    path('order/active', views.ActiveOrderListView.as_view(), name='order_list'),
    path('order/create', views.OrderCreateView.as_view(), name="order_create"),
    path('order/delivered', views.OrderDeliveredView.as_view(), name="order_delivered"),
]