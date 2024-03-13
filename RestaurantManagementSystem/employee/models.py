from django.db import models
"""from phonenumber_field.modelfields import PhoneNumberField"""
from order.models import Order
# Create your models here.
class Waiter(models.Model):
    name=models.CharField(max_length=250)
    email=models.EmailField(unique=True)
    phone_number=models.CharField(max_length=250)
    shift_choices=(('morning','Morning'),
                   ('day','Day'),('evening','Evening'))
    shift=models.CharField(max_length=250,choices=shift_choices)
    status_choices=(('free','Free'),('usy','Busy'))
    status=models.CharField(max_length=10,choices=status_choices,default='free')
    orders=models.ManyToManyField(Order, related_name='waiters')
def __str__(self):
    return self.name
