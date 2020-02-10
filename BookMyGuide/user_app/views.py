from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def loginauth(request):
    return render(request, 'login.html')

def signup_guide(request):
    return render(request, 'signup_guide.html')

def signup_tourist(request):
    # return HttpResponse('hello')
    return render(request, 'signup_tourist.html')
