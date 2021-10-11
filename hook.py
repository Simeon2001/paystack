from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
#from bal.models import fiat_wallet

# Create your views here.
@csrf_exempt
@require_POST
def pay_hook (request):
    logged = request.user

    print (request.body)
    print (request.META)

    
    return HttpResponse (status=200)

