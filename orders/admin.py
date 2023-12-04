from django.contrib import admin
from orders.models.orders import Order
from orders.models.billing_address import BillingAddress
from orders.models.guest_billing_address import Guest_BillingAddress


# Register your models here.
admin.site.register(Order)
admin.site.register(BillingAddress)
admin.site.register(Guest_BillingAddress)

