"""
Definition of models.
"""

from django.db import models


# Create your models here.



class student(models.Model): 
    eid = models.EmailField(primary_key=True) 
    uname = models.CharField(max_length=100)
    mno=models.CharField(max_length=15)
    pswd = models.CharField(max_length=20)  
    cpswd = models.CharField(max_length=20)  

    class Meta:  
        db_table = "studenttb"


class Final_HS(models.Model):
    id = models.AutoField(primary_key=True)
    eid= models.CharField(max_length=100)
    uname= models.CharField(max_length=50)
    Course= models.CharField(max_length=50)


    class Meta:  
        db_table = "Final_HS"
