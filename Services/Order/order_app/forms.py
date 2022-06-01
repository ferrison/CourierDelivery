from django import forms

from order_app import models


class OrderForm(forms.ModelForm):
    class Meta:
        model = models.Order
        fields = ["status", "address_to", "address_from", "weight", "comment"]
