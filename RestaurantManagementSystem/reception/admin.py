from django.contrib import admin
from .models import Reservation,Bill
# Register your models here.
class ReservationAdmin(admin.ModelAdmin):
    list_display=('customer_name','table','reservation_time','status')
admin.site.register(Reservation,ReservationAdmin)

class BillAdmin(admin.ModelAdmin):
    list_display=('order','total_amount','paid')
admin.site.register(Bill,BillAdmin)