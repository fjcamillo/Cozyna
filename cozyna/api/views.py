from django.shortcuts import render
from django.http import HttpResponse

#Rest
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import generic
import requests
from pprint import pprint
import json
# Create your views here.

def index(request):
    return HttpResponse('<h1>API</h1>')

class sitCounter(generic.View):

    def get(self, request, *args, **kwargs):
        if self.request.GET['hub.verify_token'] == verify_token:
            return HttpResponse(self.request.GET['hub.challenge'])
        else:
            return HttpResponse('Error', 'Invalid Token')

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args,**kwargs):
        return generic.View.dispatch(self, request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        incoming_message = json.loads(self.request.body.decode('utf-8'))
        return HttpResponse()
