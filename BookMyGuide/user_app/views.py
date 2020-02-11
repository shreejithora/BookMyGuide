from django.shortcuts import render
from django.http import HttpResponse
from .models import GuideRegisterModel, TouristRegisterModel

# Create your views here.

def loginauth(request):
    # if request.method == "POST":
    #     e = request.POST.get('email')
    #     p = request.POST.get('password')
    #     guide = GuideRegisterModel.objects.filter(email=e, password=p, is_guide=True)
    #     tourist = TouristRegisterModel.objects.filter(email=e, password=p, is_tourist=True)
    #     if(guide.count() > 0 or tourist.count() > 0 ):
    #         if(guide.is_guide == True):
    #             for user in guide:
    #                 request.session['email'] = user.email
    #                 request.session['id'] = user.id
    #                 request.session['username'] = user.username
    #                 return redirect('bmg_app:home')
    #         elif(tourist.is_tourist == True):
    #             for user in tourist:
    #                 request.session['email'] = user.email
    #                 request.session['id'] = user.id
    #                 request.session['username'] = user.username
    #                 return redirect('bmg_app:home')
    #     else:
    #         return HttpResponse('Wrong Credentials')
    # else:
        return render(request, 'login.html')

def signup_guide(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        bio_desc = request.POST['bio_desc']
        email = request.POST['email']
        password = request.POST['password']
        password1 = request.POST['password1']
        gender = request.POST['gender']
        address = request.POST['address']
        phone = request.POST['phone']
        user_img = request.POST['user_img']
        citizenship_img = request.POST['citizenship_img']
        liscence_img = request.POST['liscence']
        languages = request.POST['languages']
        locations = request.POST['location']
        is_guide - request.POST['is_guide']
        if is_guide == 'on':
            return True
        elif is_guide == 'off':
            return False

        guide = GuideRegisterModel.objects.create(first_name=first_name, last_name=last_name, username=username, bio_desc=bio_desc, email=email, password=password, gender=gender, address=address, phone=phone, user_img=user_img, citizenship_img=citizenship_img, liscence_img=liscence_img, languages=languages, locations=locations, is_guide=is_guide)
        # guide.save()
        guide.save.m2m()

    else:
        return render(request, 'signup_guide.html')

def signup_tourist(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        gender = request.POST['gender']
        is_tourist = request.POST['is_tourist']
        if is_tourist == 'on':
            return True
        elif is_tourist == 'off':
            return False

        tourist = TouristRegisterModel.objects.create(username=username, email=email, password=password, gender=gender, is_tourist=is_tourist)
        tourist.save.m2m()

    else:
        return render(request, 'signup_tourist.html')
