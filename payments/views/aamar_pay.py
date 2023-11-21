import requests
from django.shortcuts import redirect
import uuid
from decouple import config
from orders.models.billing_address import BillingAddress
from orders.models.orders import Order

STORE_ID = config('STORE_ID')
SIGNATURE_KEY = config('SIGNATURE_KEY')



def generate_transaction_id():

    #generate transaction id by uuid module
    transaction_id=uuid.uuid4()
    return transaction_id


def initial_payment(request):

    current_user = request.user
   
    user_phone = BillingAddress.objects.get(user=current_user)

    order_qs = Order.objects.filter(user=current_user, ordered=False)
    order_total = order_qs[0].get_totals()

    tran_id = generate_transaction_id()
    
    url = "https://sandbox.aamarpay.com/index.php"

    payload = {'store_id': STORE_ID,
    'signature_key': SIGNATURE_KEY,
    'cus_name': current_user.username,
    'cus_email': current_user,
    'cus_phone': user_phone.phone,
    'amount': order_total,
    'currency': 'BDT',
    'tran_id': tran_id,
    'desc': 'test transaction',
    'success_url': config('SUCCESS_URL'),
    'fail_url': 'http://localhost/aamarpay/callback/failed.php',
    'cancel_url': 'http://localhost/aamarpay/callback/cancel.php',
    'type': 'json'
    }
    print("Success url -------------",payload['success_url'])
    print("Success tran_id -------------",payload['tran_id'])
    
    files=[]
    headers = {}

    response = requests.request("POST", url, headers=headers, data=payload, files=files)
   
    data = response.json()
    return redirect(data['payment_url'])



    
