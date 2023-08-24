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