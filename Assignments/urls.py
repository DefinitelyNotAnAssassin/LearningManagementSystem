from django.urls import path    
from Assignments import views

urlpatterns = [
    
    path('assignment_home', views.assignment_home, name='assignments home'),
    path('submit_assignment/<str:assignment_id>', views.submit_assignment, name='submit assignment'),
    path('view_assignment/<str:assignment_id>', views.view_assignment, name='view assignment'),
    path('course_assignment/<str:course_code>', views.course_assignment, name='course assignments')
]