from django import forms

from order_app import models


class OrderForm(forms.ModelForm):
    class Meta:
        model = models.Order
        fields = ["address_to", "address_from", "weight", "price", "comment"]

    def __init__(self, *args, **kwargs):
        super(OrderForm, self).__init__(*args, **kwargs)
        self.fields['comment'].required = False
