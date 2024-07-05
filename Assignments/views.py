from django.shortcuts import render, redirect
from django.db.models import Exists, OuterRef
from Assignments.models import Activity, Submission
from Course.models import Course
# Create your views here.


def assignment_home(request):
    if not request.META.get("HTTP_HX_REQUEST"):
        activities = Activity.objects.filter(course_code__enrolled_students=request.user)
        items = {
            'activities': activities
        }
        return render(request, 'Assignments/partials/assignments_home.html', context = items) 
    else:
        activities = Activity.objects.filter(course_code__enrolled_students=request.user)

        # Prepare a subquery to check for existing submissions for each activity by the request.user
        submissions_exists = Submission.objects.filter(
            activity_id=OuterRef('pk'),
            student_id=request.user
        ).values('id')

        # Annotate the activities queryset with a boolean flag indicating the existence of a submission
        activities = activities.annotate(
            has_submission=Exists(submissions_exists)
        )

        items = {
            'activities': activities
        }
        print(activities)
        return render(request, 'Assignments/assignments_home.html', context=items)

def submit_assignment(request, assignment_id):
    
    if request.method == 'POST':
        submission = Submission()
        submission.activity_id = Activity.objects.get(id=assignment_id)
        submission.student_id = request.user
        submission.answer = request.POST['answer']
        submission.save()
    return redirect('assignments home')

def course_assignment(request, course_code):
    
    if not request.META.get("HTTP_HX_REQUEST"):
        activities = Activity.objects.filter(course_code=Course.objects.get(course_code=course_code))
        items = {
            'activities': activities
        }
        return render(request, 'Assignments/partials/course_assignment.html', context=items)
    else:
        activities = Activity.objects.filter(course_code=Course.objects.get(course_code=course_code))
        items = {
            'activities': activities
        }
        return render(request, 'Assignments/course_assignment.html', context=items)

def view_assignment(request, assignment_id):
    if not request.META.get("HTTP_HX_REQUEST"):
        assignment = Activity.objects.get(id=assignment_id)
        submissions = Submission.objects.filter(activity_id=assignment, student_id=request.user)
        items = {
            'activity': assignment,
            'submissions': submissions
        }
        return render(request, 'Assignments/partials/view_assignment.html', context=items)
    else:
        assignment = Activity.objects.get(id=assignment_id)
        submissions = Submission.objects.filter(activity_id=assignment, student_id=request.user)
        items = {
            'activity': assignment,
            'submissions': submissions
        }
        return render(request, 'Assignments/view_assignment.html', context=items)