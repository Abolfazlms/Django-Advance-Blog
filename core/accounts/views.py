# from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
# import time
from .tasks import sendEmail
import requests
from django.core.cache import cache
# Create your views here.
def send_email(request):
    sendEmail.delay()
    return HttpResponse("<h1>Done Sending!</h1>")
def test(request):
    if cache.get("test_delay_api") is None:
        response = requests.get("https://3f48f35a-a3db-49a2-8eff-a1a6fae38d12.mock.pstmn.io/test/delay/5")
        cache.set("test_delay_api",response.json())
        # cache.set("test_delay_api",response.json(),30)
    return JsonResponse(cache.get("test_delay_api"))
