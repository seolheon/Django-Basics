from django.shortcuts import render
from django.http import HttpResponse
import datetime

def index(request):
    return HttpResponse('Hello!')

def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>Текущая дата и время: {0}</body></html>".format(now)
    return HttpResponse(html)