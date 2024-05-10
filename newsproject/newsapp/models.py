from django.db import models

class student(models.Model):
    sno=models.IntegerField()
    sname=models.CharField(max_length=150)
    mark=models.FloatField()
