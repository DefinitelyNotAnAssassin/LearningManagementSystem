from django.shortcuts import render
from django.db.models import Avg, F, ExpressionWrapper, FloatField
from Assignments.models import Activity, Submission
from Course.models import Course
# Create your views here.


def grades_home(request):
    courses = Course.objects.filter(enrolled_students=request.user)
    print(courses)
    
    course_grades = []
    
    for course in courses:
        activities = Activity.objects.filter(course_code=course)
        course_grade = 0
        total_max_grade = 0
        for activity in activities:
            submission = Submission.objects.filter(activity_id=activity, student_id=request.user)
            if submission:
                for sub in submission:
                    course_grade += sub.submission_grade
                    total_max_grade += activity.activity_max_grade
    
        if total_max_grade > 0:
            course_grade_percentage = (course_grade / total_max_grade) * 100
        else:
            course_grade_percentage = 0
    
        course_grades.append({'course': course.course_code, 'course_name' : course.course_name, 'grade': round(course_grade_percentage, 2)})
    
    
    items = {
        'course_grades': course_grades
    }

    return render(request, 'Grades/grades_home.html', context=items)
    
