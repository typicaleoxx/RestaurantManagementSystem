from django.contrib import admin
from .models import Waiter
# Register your models here.
class WaiterAdmin(admin.ModelAdmin):
    list_display=('name','email','phone_number','shift','status')
admin.site.register(Waiter,WaiterAdmin)