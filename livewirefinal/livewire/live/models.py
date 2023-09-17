from django.db import models

# Create your models here.
class Livedata(models.Model):
    type=models.CharField(max_length=2080,default='java')
    name=models.CharField(max_length=2080)
    des1=models.TextField()
    intro_img=models.CharField(max_length=2080)
    duration=models.IntegerField()
    name2=models.CharField(max_length=2080)
    des2=models.TextField()
    objective=models.TextField()
    keytopic1=models.TextField()
    keytopic2=models.TextField()
    suitable=models.TextField(default='1')
    jobroles=models.TextField(default='1')
    scope=models.TextField()
    range1=models.IntegerField()
    range2=models.IntegerField()
    projectexp=models.TextField()

class Contacts(models.Model):
    name=models.CharField(max_length=30)
    email=models.EmailField()
    phone=models.CharField(max_length=10)
    message=models.TextField()

class Enquiry(models.Model):
    lname=models.CharField(max_length=30)
    email=models.EmailField()
    no=models.CharField(max_length=30)
    country=models.CharField(max_length=30)
    state=models.CharField(max_length=30)