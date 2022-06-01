from django.urls import path

from courier_app import views

urlpatterns = [
    path('order/create', views.OrderCreateView.as_view(), name='order_create'),
    path('order/', views.OrderListView.as_view(), name='order_list'),
    path('order/take/<uuid:id>', views.OrderTakeView.as_view(), name='take_order'),
    path('order/delivered/<uuid:id>', views.OrderDeliveredView.as_view(), name='order_delivered'),
    path('order/<uuid:id>', views.OrderView.as_view(), name='order'),
]