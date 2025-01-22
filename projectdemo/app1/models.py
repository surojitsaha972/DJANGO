from django.db import models

# Create your models here.
class students(models.Model):
    name=models.CharField(max_length=10)
    last_name=models.CharField(max_length=10)
    email=models.EmailField()
    phno=models.IntegerField(max_length=10)
    
    def __str__(self):
        return self.name