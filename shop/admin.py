from django.contrib import admin

from .models import *

admin.site.register(Customer)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)
admin.site.register(FastOrder)


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 1

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ( "date_ordered", "complete", "transaction_id", "customer","payment_type")
    inlines = [OrderItemInline,]
