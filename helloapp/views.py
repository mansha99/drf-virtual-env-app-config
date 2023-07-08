from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
def hello_world(request):
    message = settings.MESSAGE
    return HttpResponse(message)