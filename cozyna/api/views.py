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

class table_one_startSit(generic.View):
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

class table_two_startSit(generic.View):
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

class table_three_startSit(generic.View):
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

class table_four_startSit(generic.View):
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

class table_five_startSit(generic.View):
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

class table_six_startSit(generic.View):
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

class table_seven_startSit(generic.View):
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

class table_eight_startSit(generic.View):
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

class table_nine_startSit(generic.View):
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

class table_ten_startSit(generic.View):
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

class table_eleven_startSit(generic.View):
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

class table_twelve_startSit(generic.View):
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

class table_thirteen_startSit(generic.View):
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

class table_fourteen_startSit(generic.View):
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

class table_fifteen_startSit(generic.View):
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

class table_sixteen_startSit(generic.View):
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

class table_seventeen_startSit(generic.View):
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

class table_eighteen_startSit(generic.View):
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

class table_nineteen_startSit(generic.View):
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

class table_twenty_startSit(generic.View):
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


#===============================================================================

class table_one_ordered(generic.View):
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

class table_two_ordered(generic.View):
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

class table_three_ordered(generic.View):
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

class table_four_ordered(generic.View):
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

class table_five_ordered(generic.View):
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

class table_six_ordered(generic.View):
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

class table_seven_ordered(generic.View):
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

class table_eight_ordered(generic.View):
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

class table_nine_ordered(generic.View):
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

class table_ten_ordered(generic.View):
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

class table_eleven_ordered(generic.View):
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


class table_twelve_ordered(generic.View):
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

class table_thirteen_ordered(generic.View):
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

class table_fourteen_ordered(generic.View):
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

class table_fifteen_ordered(generic.View):
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

class table_sixteen_ordered(generic.View):
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

class table_seventeen_ordered(generic.View):
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

class table_eighteen_ordered(generic.View):
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

class table_nineteen_ordered(generic.View):
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

class table_twenty_ordered(generic.View):
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

#===============================================================================


class table_one_arrived(generic.View):
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

class table_two_arrived(generic.View):
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


class table_three_arrived(generic.View):
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


class table_four_arrived(generic.View):
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


class table_five_arrived(generic.View):
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


class table_six_arrived(generic.View):
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


class table_seven_arrived(generic.View):
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


class table_eight_arrived(generic.View):
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


class table_nine_arrived(generic.View):
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


class table_ten_arrived(generic.View):
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


class table_eleven_arrived(generic.View):
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


class table_twelve_arrived(generic.View):
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


class table_thirteen_arrived(generic.View):
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


class table_fourteen_arrived(generic.View):
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


class table_fifteen_arrived(generic.View):
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


class table_sixteen_arrived(generic.View):
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


class table_seventeen_arrived(generic.View):
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


class table_eighteen_arrived(generic.View):
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


class table_nineteen_arrived(generic.View):
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


class table_twenty_arrived(generic.View):
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

#===============================================================================

class table_one_finished(generic.View):
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

class table_two_finished(generic.View):
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

class table_three_finished(generic.View):
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

class table_four_finished(generic.View):
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

class table_five_finished(generic.View):
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

class table_six_finished(generic.View):
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

class table_seven_finished(generic.View):
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

class table_eight_finished(generic.View):
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

class table_nine_finished(generic.View):
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

class table_ten_finished(generic.View):
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

class table_eleven_finished(generic.View):
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

class table_twelve_finished(generic.View):
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

class table_thirteen_finished(generic.View):
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

class table_fourteen_finished(generic.View):
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

class table_fifteen_finished(generic.View):
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

class table_sixteen_finished(generic.View):
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

class table_seventeen_finished(generic.View):
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

class table_eighteen_finished(generic.View):
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

class table_nineteen_finished(generic.View):
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

class table_twenty_finished(generic.View):
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

#===============================================================================

class table_one_endSit(generic.View):
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

class table_two_endSit(generic.View):
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

class table_three_endSit(generic.View):
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

class table_four_endSit(generic.View):
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

class table_five_endSit(generic.View):
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

class table_six_endSit(generic.View):
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

class table_seven_endSit(generic.View):
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

class table_eight_endSit(generic.View):
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

class table_nine_endSit(generic.View):
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

class table_ten_endSit(generic.View):
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

class table_eleven_endSit(generic.View):
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

class table_twelve_endSit(generic.View):
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

class table_thirteen_endSit(generic.View):
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

class table_fourteen_endSit(generic.View):
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

class table_fifteen_endSit(generic.View):
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

class table_sixteen_endSit(generic.View):
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

class table_seventeen_endSit(generic.View):
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

class table_eighteen_endSit(generic.View):
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

class table_nineteen_endSit(generic.View):
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

class table_twenty_endSit(generic.View):
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

class table_one_endSit(generic.View):
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
