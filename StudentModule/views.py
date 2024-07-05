from django.shortcuts import render
from Course.models import Course

# Create your views here.


def student_home(request):
    if request.META.get("HTTP_HX_REQUEST"):
        items = {
            'courses': Course.objects.filter(enrolled_students=request.user)
        }
        return render(request, 'StudentModule/partials/student_home.html', context=items)
    else:   
        items = {
            'courses': Course.objects.filter(enrolled_students=request.user)
        }
        return render(request, 'StudentModule/student_home.html', context=items)