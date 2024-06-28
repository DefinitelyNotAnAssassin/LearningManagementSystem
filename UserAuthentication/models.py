from django.db import models
from django.contrib.auth.models import AbstractUser 


class Account(AbstractUser): 
    role = models.CharField(max_length=50)
    level = models.CharField(max_length=50)
    picture = models.ImageField(upload_to='profile_pictures')
    
    def __str__(self):
        return self.username