import requests
from django.shortcuts import render

# Create your views here.
from django.views import generic

from order_app import models, forms


class OrderCreateView(generic.CreateView):
    template_name = 'order_create.html'
    model = models.Order
    form_class = forms.OrderForm

    def form_valid(self, form):
        requests.post('http://courier:8001/order/create', data={"id": form.instance.id,
                                                                "address_from": form.instance.address_from,
                                                                "address_to": form.instance.address_to,
                                                                "weight": form.instance.weight,
                                                                "comment": form.instance.comment})
        return super().form_valid(form)
