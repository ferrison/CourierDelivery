import requests
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.utils.decorators import method_decorator
from django.views import generic, View
from django.views.decorators.csrf import csrf_exempt

from order_app import models, forms
from order_app.models import Order


class OrderCreateView(generic.CreateView):
    template_name = 'order_create.html'
    model = models.Order
    form_class = forms.OrderForm

    def form_valid(self, form):
        form.instance.client = self.request.user
        requests.post('http://courier:8001/order/create', data={"id": form.instance.id,
                                                                "address_from": form.instance.address_from,
                                                                "address_to": form.instance.address_to,
                                                                "weight": form.instance.weight,
                                                                "comment": form.instance.comment})
        return super().form_valid(form)


class OrderListView(generic.ListView):
    template_name = 'order_list.html'
    model = Order
    context_object_name = 'order_list'

    def get_queryset(self):
        print(self.request.user)
        return Order.objects.filter(client=self.request.user)


@method_decorator(csrf_exempt, name='dispatch')
class OrderDeliveredView(View):
    def post(self, request):
        order = Order.objects.get(id=request.POST['id'])
        order.status = 'delivered'
        order.save()
        return HttpResponse()
