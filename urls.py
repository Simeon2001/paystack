from django.urls import path
from . import hook
from pay.settings import WEBHOOK_URL

urlpatterns = [
    path (WEBHOOK_URL, hook.pay_hook, name = 'hook/' ),
    
    
]