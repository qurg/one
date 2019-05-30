from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
from stock.tasks import update_data


def index(request):
    update_data.delay(1, '000002')
    return HttpResponse('Hello Celery')
