from django.db import models
from django.core.validators import MinLengthValidator
from datetime import datetime  
# Create your models here.


class Employees(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    address = models.TextField()
    phone = models.CharField(max_length=10)
    

    def __str__(self):
        return self.name


class Child(models.Model):
    name = models.ForeignKey(Employees, null=True,on_delete=models.CASCADE)
    email = models.EmailField(max_length=200)
    address = models.TextField()
    phone = models.CharField(max_length=10)
    time = models.DateTimeField(default=datetime.now(), blank=True)

    def __str__(self):
        return self.email

    
