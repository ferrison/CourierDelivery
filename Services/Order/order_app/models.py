import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models


class Client(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)


class Order(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    status = models.CharField(choices=(("published", "published"),
                                       ("accepted", "accepted"),
                                       ("declined", "declined"),
                                       ("delivered", "delivered")),
                              max_length=20)
    address_from = models.CharField(max_length=500)
    address_to = models.CharField(max_length=500)

    created_at = models.DateTimeField(auto_now_add=True)


class Position(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=80)
    quantity = models.IntegerField()
    order = models.ForeignKey('Order', on_delete=models.CASCADE)
