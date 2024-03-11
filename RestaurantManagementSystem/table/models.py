from django.db import models

# Create your models here.
class Table(models.Model):
    number=models.IntegerField()
    capacity=models.IntegerField()
    status_choices=(('available','Available'),('reserved','Reserved'),('occupied','Occupied'))
    status=models.CharField(max_length=250,choices=status_choices)