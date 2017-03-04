from django.shortcuts import render
from django.http import HttpResponse

#Rest
from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

# from django.
from django.views import generic
import requests
from pprint import pprint
import json
# Create your views here.

def index(request):
    return HttpResponse('<h1>API</h1>')

class sitCounter(generic.View):
    @csrf_exempt
    def dispatch(self, request, *args,**kwargs):
        return generic.View.dispatch(self, request, *args, **kwargs)

    # @method_decorator(csrf_excempt)
    # @ensure_csrf_cookie
    # @method_decorator(ensure_csrf_cookie)
    def post(self, request, *args, **kwargs):
        incoming_message = json.loads(self.request.body.decode('utf-8'))
        pprint(incoming_message)
        return HttpResponse()
