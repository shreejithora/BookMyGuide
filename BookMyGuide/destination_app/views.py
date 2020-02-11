from django.shortcuts import render
from .models import HireModel

# Create your views here.

def hireform(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        pick_date = request.POST['pick_date']
        full_address = request.POST['full_address']
        phone = request.POST['phone']
        tour = request.POST['tour']

        hire = HireModel.object.create(username=username,
                                        email=email,
                                        pick_date=pick_date,
                                        full_address=full_address,
                                        address=address,
                                        phone=phone,
                                        tour=tour)
        hire.save()
    else:
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
