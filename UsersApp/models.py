from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.

class Users(models.Model):
    UserId=models.AutoField(primary_key=True)
    UserName=models.CharField(max_length=200)
    Email=models.EmailField()
    Password=models.CharField(max_length=20)
    Phone=models.CharField(max_length=15)
    DateOfCreation=models.DateField()

class Strategies(models.Model):
   # sNo=models.AutoField(primary_key=True)
    id=models.AutoField(primary_key=True)
   # id=models.IntegerField(primary_key=True)
    sName=models.CharField(max_length=50)
    symbol=models.CharField(max_length=20)
    entryType=models.CharField(max_length=10)
    orderType=models.CharField(max_length=12)

