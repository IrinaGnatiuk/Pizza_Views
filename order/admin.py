from django.contrib import admin
from order.models import Order, ShippingOrder
from dishes.models import InstanceDish


class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'full_price', 'user']
    # readonly_fields = ['price']


admin.site.register(Order, OrderAdmin)
admin.site.register(ShippingOrder)

