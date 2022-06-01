from django.urls import path

from order_app import views

urlpatterns = [
    path('order/create', views.OrderCreateView.as_view(), name="order_create"),
]