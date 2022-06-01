from celery import shared_task

from courier_app.models import Courier


@shared_task
def create_order(req):
    couriers = Courier.objects.filter(status='free').order_by('?').first()
    print(couriers)
