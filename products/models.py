from django.db import models

# Create your models here.
class Mobiles(models.Model):
     name=models.CharField(max_length=200,unique=True)
     brand=models.CharField(max_length=200)
     specs=models.CharField(max_length=150)
     price=models.IntegerField()
     
     def   __str__(self):
          return self.name