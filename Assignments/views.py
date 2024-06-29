from django.shortcuts import render
from Assignments.models import Activity, Submission
# Create your views here.


def assignment_home(request):
    # get all of the activity of the course where the student is enrolled
    
    activities = Activity.objects.filter(course_code__enrolled_students=request.user)
    items = {
        'activities': activities
    }
    print(activities)
    return render(request, 'Assignments/assignments_home.html', context=items)

def submit_assignment(request):
    return render(request, 'Assignments/submit_assignment.html')

def view_assignment(request):
    return render(request, 'Assignments/view_assignment.html')