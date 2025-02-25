from django.db import models



class user(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)
    mobile = models.CharField(max_length=100)
    class Meta:
        db_table = 'user'

class student(models.Model):
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    address= models.CharField(max_length=100)
    pin = models.IntegerField()
    password = models.CharField(max_length=100)
    city= models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone_no = models.IntegerField()
    father_name = models.CharField(max_length=100)
    mother_name = models.CharField(max_length=100)
    tenth_marks = models.IntegerField()
    twelth_marks = models.IntegerField()
    subject = models.CharField(max_length=100)
    isApproved = models.BooleanField(default=False) 
    class Meta:
        db_table = 'student'