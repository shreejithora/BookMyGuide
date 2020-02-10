from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, 'index.html')

def ourservices(request):
    return render(request, 'ourservices.html')

def whyus(request):
    return render(request, 'whyus.html')

def store(request):
    return render(request, 'store.html')
