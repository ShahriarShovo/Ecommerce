from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from payments.models.aamar_pay_data import aamar_pay_data
from payments.views.amar_pay.product_purchased import product_purchased
from django.shortcuts import HttpResponseRedirect
from django.urls import reverse




@csrf_exempt
def success(request):
    
    if request.method=='POST' or request.method=='post':
        payment_data=request.POST
        print("Payment data_________________",payment_data)
        email = payment_data['cus_email']
        txnid= payment_data['mer_txnid']
        pg_txnid = payment_data['pg_txnid']
        ip_address = payment_data['ip_address']
        card_type=payment_data['card_type']
        total_amount=payment_data['amount_original']
        print("amount_original-------------", total_amount)

        convert_data = payment_data.dict()
        saved_data = aamar_pay_data.objects.create(email=email, datas=convert_data)

        
        return HttpResponseRedirect(reverse('product_purchased', kwargs={'order_id':pg_txnid,
                                                                         'payment_id':txnid,
                                                                         'ip_address': ip_address,
                                                                         'card_type':card_type,},))
        
    else:
        return HttpResponse("Not okay")
