from django.urls import path 
from Course import views 

urlpatterns = [ 
               path('course_home', views.course_home, name='course home'),
               path('enroll_course', views.enroll_course, name='enrolled course'),
               path('view_course/<int:course_id>', views.view_course, name='view course'),
               path('view_material/<int:material_id>', views.view_material, name='view material'),]
