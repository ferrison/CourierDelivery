import os

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Courier.settings')

app = Celery('Courier', broker='amqp://guest:guest@rabbitmq')

app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')

