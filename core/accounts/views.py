# from django.shortcuts import render
# import time
import requests
from django.http import HttpResponse, JsonResponse

# from django.core.cache import cache
from django.views.decorators.cache import cache_page
from .tasks import sendEmail


# Create your views here.
def send_email(request):
    sendEmail.delay()
    return HttpResponse("<h1>Done Sending!</h1>")


# def test(request):
#     if cache.get("test_delay_api") is None:
#         response = requests.get("https://3f48f35a-a3db-49a2-8eff-a1a6fae38d12.mock.pstmn.io/test/delay/5")
#         cache.set("test_delay_api",response.json())
#         # cache.set("test_delay_api",response.json(),30)
#     return JsonResponse(cache.get("test_delay_api"))
@cache_page(60)
def test(request):
    response = requests.get(
        "https://3f48f35a-a3db-49a2-8eff-a1a6fae38d12.mock.pstmn.io/test/delay/5"
    )
    return JsonResponse(response.json())
