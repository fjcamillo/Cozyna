from django.shortcuts import render
from django.http import HttpResponse

from api.models import arrived, entered, finished, left, order, sat

# Create your views here.

def index(request):
    arrivedCustomer = arrived.objects.all()
    enteredCustomer = entered.objects.all()
    finishedCustomer = finished.objects.all()
    leftCustomer = left.objects.all()
    orderCustomer = order.objects.all()
    satCustomer = sat.objects.all()
    va = 0
    context = {
        'arrivedCustomer': arrivedCustomer,
        'va': va
    }
    # return render(request, 'home/index.html', context)
    return render(request, 'home/index.html', context)
