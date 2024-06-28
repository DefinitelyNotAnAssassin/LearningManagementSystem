from django.urls import path    
from Assignments import views

urlpatterns = [
    
    path('assignment_home', views.assignment_home, name='assignments home'),
    path('submit_assignment', views.submit_assignment, name='submit assignment'),
    path('view_assignment', views.view_assignment, name='view assignment'),
]