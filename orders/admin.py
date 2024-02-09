from django.contrib import admin
from orders.models.orders import Order
from orders.models.billing_address import BillingAddress
from orders.models.guest_billing_address import Guest_BillingAddress

from orders.models.product_ordered import Products_Ordered


# Register your models here.
admin.site.register(Order)
admin.site.register(BillingAddress)
admin.site.register(Guest_BillingAddress)

admin.site.register(Products_Ordered)

