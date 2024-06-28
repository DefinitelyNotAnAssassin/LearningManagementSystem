from django.urls import path
from Grades import views

urlpatterns = [
     path('grades_home', views.grades_home, name='grades home'),
]
