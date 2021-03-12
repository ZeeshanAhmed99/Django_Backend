from django.db import models

class formdata(models.Model):
    Name = models.CharField(max_length=50)
    Email = models.CharField(max_length=50)
    Password = models.CharField(max_length=20)     

# Create your models here.
class getdata(models.Model):
    Email = models.CharField(max_length = 50)
    
    def __str__(self):
        return getdata.Email 
    