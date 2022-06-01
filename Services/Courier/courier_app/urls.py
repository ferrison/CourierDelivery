from django.urls import path

from courier_app import views

urlpatterns = [
    path('order/create', views.OrderCreateView.as_view())
]