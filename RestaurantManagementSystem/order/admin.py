from django.contrib import admin
from .models import Order
# Register your models here.
class OrderAdmin(admin.ModelAdmin):
    list_display=('id','table',
                  'waiter',
                  'get_items_list','total_amount','status','timestamp')

    def get_items_list(self, obj):
        return ", ".join([item.name for item in obj.items.all()])
    get_items_list.short_description = "Items"

"""since items field chai manytomanyfield ho ani list_display ma we cannot directly put that field, we defined a custom method get_items_list() bhanne

 (obj.items.all()) yo method le chai items ma bhako sabai lai retrieve garcha ani euta single string ma comma le separate garera join garcha

also we set a short_description attribute for the get_items_list method to specify the column header name as 'Items
        """
admin.site.register(Order, OrderAdmin)
