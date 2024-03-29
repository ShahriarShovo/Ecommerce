from django.urls import path
from payments.views.amar_pay.aamar_pay import initial_payment 
from payments.views.amar_pay.payment_success import success
from payments.views.amar_pay.product_purchased import product_purchased
from payments.views.invoice import invoice
from payments.views.cash_on_delivery.cash_on_delivery import cash_on_delivery
from payments.views.cash_on_delivery.cash_on_delivary_for_single_product import cash_on_delivary_for_single_product


urlpatterns = [

    path('payment/', initial_payment, name='initial_payment_amarPay'),
    path('payment_sucess/', success, name='payment_success'),
    path('product_purchased/<order_id>/<payment_id>/<ip_address>/<card_type>', product_purchased, name ='product_purchased'),
    path('invoice//<pay_id>/<order_id>/', invoice, name ='invoice'),


    #cash_on_delivery
    path('cash_on_delivery/', cash_on_delivery, name ='cash_on_delivery'),
    
    path('cash_on_delivery/<int:pk>/', cash_on_delivary_for_single_product, name ='cash_on_delivary_for_single_product'),

    
    
]
