import os

from celery import Celery

app = Celery('order_app', broker='amqp://guest:guest@rabbitmq')


@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')


@app.task
def add(a, b):
    print(a+b)
