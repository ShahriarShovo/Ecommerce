from django.urls import path
from payments.views.aamar_pay import initial_payment #, success
from payments.views.payment_success import success
from payments.views.product_purchased import product_purchased
from payments.views.invoice import invoice


urlpatterns = [

    path('payment/', initial_payment, name='initial_payment_amarPay'),
    path('payment_sucess/', success, name='payment_success'),
    path('product_purchased/<val_id>/<tran_id>/', product_purchased, name ='product_purchased'),
    path('invoice/', invoice, name ='invoice'),
    
    
]
