from django.db import models
from table.models import Table
from menu.models import Menu
from employee.models import Waiter
# Create your models here.
class Order(models.Model):
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    items=models.ManyToManyField(Menu)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    status_choices=(('preparing','Preparing'),('served','Served'))
    waiter=models.ForeignKey(Waiter, on_delete=models.CASCADE,null=True)
    status=models.CharField(max_length=250,choices=status_choices)
    timestamp=models.DateTimeField()
    def __str__(self) :
        return str(self.id)