from django.shortcuts import render
from Course.models import Course, CourseMaterial
# Create your views here.

def course_home(request):
    if not request.META.get("HTTP_HX_REQUEST"):
        return render(request, 'Course/partials/course_home.html')
    else:
        return render(request, 'Course/course_home.html')

def enroll_course(request):
    if not request.META.get("HTTP_HX_REQUEST"):
        courses = Course.objects.filter(enrolled_students=request.user)
        items = { 
                'courses': courses
        }
        return render(request, 'Course/partials/course_list.html', context = items)
    else:
        
        courses = Course.objects.filter(enrolled_students=request.user)
        items = { 
                'courses': courses
        }
        return render(request, 'Course/course_list.html', context = items)


def view_course(request, course_id):
    if not request.META.get("HTTP_HX_REQUEST"):
        course = Course.objects.get(id=course_id)
        course_materials = CourseMaterial.objects.filter(course_code_id=course.id)
        items = {
                 'course': course,
                 'course_materials': course_materials
        }
        return render(request, 'Course/partials/view_course.html', context = items)
    
    else:
        course = Course.objects.get(id=course_id)
        course_materials = CourseMaterial.objects.filter(course_code_id=course.id)
        print(course_materials)
        items = {
                'course': course,
                'course_materials': course_materials
        }
        return render(request, 'Course/view_course.html', context = items)

def view_material(request, material_id):
    if not request.META.get("HTTP_HX_REQUEST"):
        material = CourseMaterial.objects.get(id=material_id)
        items = {
                 'material': material
        }
        return render(request, 'Course/partials/view_material.html', context = items)
    else:
        
        material = CourseMaterial.objects.get(id=material_id)
        items = {
                'material': material
        }
        return render(request, 'Course/view_material.html', context = items)