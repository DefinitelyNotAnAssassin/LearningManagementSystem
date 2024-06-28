from django.shortcuts import render, redirect

# Create your views here.


def index(request):
    if request.user.is_authenticated:
        return redirect('student home')
    else:
        return render(request, 'LandingPage/index.html')