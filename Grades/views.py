from django.shortcuts import render

# Create your views here.


def grades_home(request):
    return render(request, 'Grades/grades_home.html')