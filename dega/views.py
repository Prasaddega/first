from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def prasad(request):
    return HttpResponse('<marquee><h1>i am prasad dega</h1></marquee>')