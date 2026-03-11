from django.db import models

# Create your models here.
# 1st way -> Admin model, student model
# 2nd way -> User -> role-admin,student

class User(models.Model):
    role = models.CharField(max_length=15)
    username = models.CharField(max_length=30)
    address = models.CharField(max_length=45)
    phone_number = models.CharField(max_length=12)
    password = models.CharField(max_length=15,default='root')

class Course(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()
    student = models.ManyToManyField(User,blank=True)