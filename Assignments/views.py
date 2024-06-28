from django.shortcuts import render

# Create your views here.


def assignment_home(request):
    return render(request, 'Assignments/assignments_home.html')

def submit_assignment(request):
    return render(request, 'Assignments/submit_assignment.html')

def view_assignment(request):
    return render(request, 'Assignments/view_assignment.html')