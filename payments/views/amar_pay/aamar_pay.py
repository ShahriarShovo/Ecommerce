import requests
from django.shortcuts import redirect, HttpResponse
import uuid
from decouple import config
from orders.models.billing_address import BillingAddress
from orders.models.orders import Order
from cart.models.cart import Cart
STORE_ID = config('STORE_ID')
SIGNATURE_KEY = config('SIGNATURE_KEY')



def generate_transaction_id():

    #generate transaction id by uuid module
    transaction_id=uuid.uuid4()
    return transaction_id


def initial_payment(request):


    if request.user.is_authenticated:

        current_user = request.user
    
        # user_phone = BillingAddress.objects.get(user=current_user)
        # get_total_all=request.session['get_total_all']

        order_qs = Cart.objects.filter(user=current_user, is_paid=False)
        order_total = order_qs[0].get_fully_total()

        print("Total -------------", order_total)
        # print("Session get_total_all ++++++++++++++++++++", get_total_all)


        tran_id = generate_transaction_id()
        
        url = "https://sandbox.aamarpay.com/index.php"

        payload = {'store_id': STORE_ID,
        'signature_key': SIGNATURE_KEY,
        'cus_name': current_user.username,
        'cus_email': current_user,
        'cus_phone': "None",
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
        print("Response from Amar pay -----------------------", data)
        return redirect(data['payment_url'])
    
    # else:

    #     get_total_all=request.session['get_total_all']
    #     cus_name = request.session['first_name']
    #     email = request.session['email']
    #     phone = request.session['phone']
    #     print("Session get_total_all ++++++++++++++++++++", get_total_all)
    #     print("Session get_name ++++++++++++++++++++", cus_name)
    #     print("Session get_email ++++++++++++++++++++", email)

    #     tran_id = generate_transaction_id()
        
    #     url = "https://sandbox.aamarpay.com/index.php"

    #     payload = {'store_id': STORE_ID,
    #     'signature_key': SIGNATURE_KEY,
    #     'cus_name': cus_name,
    #     'cus_email': email,
    #     'cus_phone': phone,
    #     'amount': get_total_all,
    #     'currency': 'BDT',
    #     'tran_id': tran_id,
    #     'desc': 'test transaction',
    #     'success_url': config('SUCCESS_URL'),
    #     'fail_url': 'http://localhost/aamarpay/callback/failed.php',
    #     'cancel_url': 'http://localhost/aamarpay/callback/cancel.php',
    #     'type': 'json'
    #     }
    #     print("Success url -------------",payload['success_url'])
    #     print("Success tran_id -------------",payload['tran_id'])
        
    #     files=[]
    #     headers = {}
    #     response = requests.request("POST", url, headers=headers, data=payload, files=files)
    #     data = response.json()
    #     print("Response from Amar pay -----------------------", data)
    #     return redirect(data['payment_url'])

        



    
