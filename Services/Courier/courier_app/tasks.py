from celery import shared_task

from courier_app.models import Courier


@shared_task
def create_order(id, address_from, address_to, weight, comment):
    couriers = Courier.objects.filter(status='free').order_by('?').first()
    print(couriers)
