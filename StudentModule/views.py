from django.shortcuts import render

# Create your views here.


def student_home(request):
    if request.META.get("HTTP_HX_REQUEST"):
        return render(request, 'StudentModule/partials/student_home.html')
    else:   
        return render(request, 'StudentModule/student_home.html')