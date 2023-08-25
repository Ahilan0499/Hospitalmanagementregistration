from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    name=models.CharField(max_length=255)
    email=models.CharField(max_length=255,unique=True)
    password=models.CharField(max_length=255)
    date = models.DateField('Date', blank=True, null=True)
    time=models.TimeField('Time' , blank=True,null=True)
    phonenumber = models.CharField(max_length=15, null=True, blank=True)
    gender=models.CharField(max_length=255,default="SOME STRING")
    location=models.CharField(max_length=255,default="SOME STRING")
    dob=models.DateField('dateofbirth', blank=True,null=True)
    maritalstatus=models.CharField(max_length=255,default="SOME STRING")
    occupation=models.CharField(max_length=255,default="SOME STRING")

    username=None

    USERNAME_FIELD='email'
    REQUIRED_FIELDS=[]

# Create your models here.
