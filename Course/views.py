from django.shortcuts import render
from Course.models import Course, CourseMaterial
# Create your views here.

def course_home(request):
    return render(request, 'Course/course_home.html')

def enroll_course(request):
    courses = Course.objects.filter(enrolled_students=request.user)
    items = { 
             'courses': courses
    }
    return render(request, 'Course/course_list.html', context = items)


def view_course(request, course_id):
    course = Course.objects.get(id=course_id)
    course_materials = CourseMaterial.objects.filter(course_code_id=course.id)
    print(course_materials)
    items = {
             'course': course,
             'course_materials': course_materials
    }
    return render(request, 'Course/view_course.html', context = items)