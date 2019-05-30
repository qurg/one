from celery import shared_task
from .models import *
import time


@shared_task
def update_data(index_id, value):
    Index.objects.filter(id=index_id).update(code=value)


@shared_task
def timing():
    now = time.strftime("%H:%M:%S")
    with open("out.txt","a") as f:
        f.write("The time is " + now)
        f.write("\n")
        f.close()

