from django.http import HttpResponse
from django.shortcuts import render
from django.utils.decorators import method_decorator

from django.views import generic, View
from courier_app.tasks import create_order


# Create your views here.
from django.views.decorators.csrf import csrf_exempt


@method_decorator(csrf_exempt, name='dispatch')
class OrderCreateView(View):
    def post(self, request):
        print(request.POST)
        create_order.delay(1,1,1,1,1)
        return HttpResponse()
