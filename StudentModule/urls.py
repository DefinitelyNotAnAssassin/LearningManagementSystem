from django.urls import path 
from StudentModule import views 

urlpatterns = [
     path('student_home', views.student_home, name='student home'),
]
