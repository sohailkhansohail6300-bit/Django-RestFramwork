from django.db import models

# Create your models here.

class Student(models.Model):
    name=models.CharField(max_length=50,null=True)
    age=models.DateField(auto_now=False, auto_now_add=False,null=True)
    Department=models.CharField(null=True, max_length=50)