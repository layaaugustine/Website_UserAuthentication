from django.db import models

# Create your models here.

class user(models.Model):
    Username = models.CharField(max_length=50)
    FirstName = models.CharField(max_length=50)
    LastName = models.CharField(max_length=50)
    Email = models.EmailField()
    Password = models.CharField(max_length=50)
    ConfirmPassword = models.CharField(max_length=50)
