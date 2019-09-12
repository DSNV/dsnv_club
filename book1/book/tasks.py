import time
from celery import shared_task


@shared_task()
def hello(num):
    for i in range(num):
        print('hello')
        time.sleep(1)