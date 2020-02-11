from django.shortcuts import render, redirect
from .models import HireModel,DestinationModel
from django.contrib.auth.decorators import login_required

# Create your views here.
# @login_required
def hireform(request):
    if 'id' in request.session:
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
    else:
        return redirect('user:login')

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
    if request.method == "POST":
        qs = DestinationModel.objects.all()
        name_query = request.GET.get('name')

        if name_query != '' and name_query is not None:
            qs = qs.filter(destination__icontains = name_query)

        context= {
            'queryset' : qs
        }
        return render(request, 'trekandtour.html', context)
    else:
        qs = DestinationModel.objects.all()
        context= {
            'queryset' : qs
        }

        return render(request, 'trekandtour.html', context)

def tour(request):
    return render(request, 'tour.html')

def richa(request):
    return render(request, 'richa.html')
