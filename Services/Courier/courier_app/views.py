import requests
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator

from django.views import generic, View

from courier_app.models import Order
from courier_app.tasks import create_order


from django.views.decorators.csrf import csrf_exempt


@method_decorator(csrf_exempt, name='dispatch')
class OrderCreateView(View):
    def post(self, request):
        order = Order.objects.create(id=request.POST['id'],
                                     address_from=request.POST['address_from'],
                                     address_to=request.POST['address_to'],
                                     weight=request.POST['weight'],
                                     comment=request.POST['comment'])
        order.save()
        return HttpResponse()


class OrderTakeView(View):
    def get(self, request, id):
        order = Order.objects.get(id=id)
        order.status = 'in_process'
        order.courier = request.user
        order.save()
        requests.post('http://order:8000/order/accepted', {"id": id})
        return redirect('order', id=id)


class OrderDeliveredView(View):
    def get(self, request, id):
        order = Order.objects.get(id=id)
        order.status = 'delivered'
        order.save()
        requests.post('http://order:8000/order/delivered', {"id": id})
        return redirect('order_list')


class OrderView(generic.DetailView):
    pk_url_kwarg = 'id'
    model = Order
    template_name = 'order.html'


class OrderListView(generic.ListView):
    template_name = 'order_list_accepted.html'
    model = Order
    context_object_name = 'order_list'

    def get_queryset(self):
        return Order.objects.filter(status='created')
