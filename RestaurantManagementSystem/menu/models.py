from django.db import models


# Create your models here.

class Menu(models.Model):
    category_choices = (
        ("appetizers", "Appetizers"),
        ("main_course", "Main Course"),
        ("beverages", "Beverages"),
        ("desert", "Desert"),
    )
    category = models.CharField(max_length=30, choices=category_choices)
    name = models.CharField(max_length=250,unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(unique=True)

    def __str__(self):
        return self.name
