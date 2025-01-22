from django.db import models
class student(models.Model):
    name=models.CharField(max_length=20)
    Roll=models.IntegerField(max_length=20)
    Stream=models.CharField(max_length=20)
    RegNo=models.IntegerField(max_length=20)

# Create your models here.
