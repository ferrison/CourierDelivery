import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models


class Courier(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    rating_sum = models.IntegerField(default=0)
    rating_quantity = models.IntegerField(default=0)

    def rating(self):
        return self.rating_sum/self.rating_quantity if self.rating_quantity != 0 else 0
