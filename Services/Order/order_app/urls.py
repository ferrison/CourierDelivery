from django.urls import path

from order_app import views

urlpatterns = [
    path('order/<uuid:id>', views.OrderDetailView.as_view(), name='order_detail'),
    path('order/active', views.ActiveOrderListView.as_view(), name='order_list_accepted'),
    path('order/history', views.HistoryOrderListView.as_view(), name='order_list_history'),
    path('order/create', views.OrderCreateView.as_view(), name="order_create"),
    path('order/accepted', views.OrderAcceptedView.as_view(), name="order_accepted"),
    path('order/delivered', views.OrderDeliveredView.as_view(), name="order_delivered"),
]