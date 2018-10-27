from django.db import models

# Create your models here.
class Student(models.Model):
    s_name = models.CharField(max_length=10,unique=True)
    s_age = models.IntegerField(default=19)
    s_sex = models.BooleanField(default=1)