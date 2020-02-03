from django.shortcuts import render

# Create your views here.
def UserAuth(request):
        return render(request, 'login.html')