from django.shortcuts import render

# Create your views here.

def hireform(request):
    return render(request, 'hireform.html')

def findaguide(request):
    return render(request, 'findaguide.html')

def annapurna(request):
    return render(request, 'annapurna.html')

def everest(request):
    return render(request, 'everest.html')

def kathmandu(request):
    return render(request, 'kathmandu.html')

def bhaktapur(request):
    return render(request, 'bhaktapur.html')

def trekandtour(request):
    return render(request, 'trekandtour.html')

def tour(request):
    return render(request, 'tour.html')

def richa(request):
    return render(request, 'richa.html')
