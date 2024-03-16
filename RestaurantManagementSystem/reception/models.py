from django.db import models
from table.models import Table
from order.models import Order


# Create your models here.
class Reservation(models.Model):
    customer_name = models.CharField(("name"), max_length=250)
    table = models.ForeignKey(Table, on_delete=models.SET_NULL, null=True)
    reservation_time = models.DateTimeField()
    status_choices = (("confirmed", "Confirmed"), ("canceled", "Canceled"))
    status = models.CharField(max_length=50, choices=status_choices)
    def str(self):
        return self.customer_name

class Bill(models.Model):
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    total_amount = models.DecimalField(max_digits=19, decimal_places=2)
    paid = models.BooleanField()
    def str(self):
        return str(self.order)
