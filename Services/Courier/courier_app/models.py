import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models


class Courier(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    status = models.CharField(choices=(('free', 'free'), ('working', 'working')), max_length=10, default='free')
    rating_sum = models.IntegerField(default=0)
    rating_quantity = models.IntegerField(default=0)

    def rating(self):
        return self.rating_sum/self.rating_quantity if self.rating_quantity != 0 else 0


class Order(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    status = models.CharField(choices=(('created', 'created'),
                                       ('in_process', 'in_process'),
                                       ('delivered', 'delivered')),
                              max_length=10,
                              default='created')
    address_from = models.CharField(max_length=500)
    address_to = models.CharField(max_length=500)
    weight = models.FloatField()
    comment = models.TextField()
    courier = models.ForeignKey('Courier', on_delete=models.DO_NOTHING, null=True, blank=True, default=None)
