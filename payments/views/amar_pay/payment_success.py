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
        email = payment_data['cus_email']
        txnid= payment_data['mer_txnid']
        pg_txnid = payment_data['pg_txnid']
        total_amount=payment_data['amount_original']
        print("amount_original-------------", total_amount)

        convert_data = payment_data.dict()
        saved_data = aamar_pay_data.objects.create(email=email, datas=convert_data)


        return HttpResponseRedirect(reverse('product_purchased', kwargs={'val_id':pg_txnid, 'tran_id':txnid, 'total_amount':total_amount,},))
        
    else:
        return HttpResponse("Not okay")
