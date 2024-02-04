from django.shortcuts import redirect, HttpResponse, HttpResponseRedirect
from django.urls import reverse


def choose_payment(request):

    if request.method=="POST":
        selected_payment_method=request.POST.get('select_option')

        if selected_payment_method == 'cash_on_delivary':
            #print("cash_on_delivary +++++++++++++++", selected_payment_method)
            return HttpResponseRedirect(reverse('cash_on_delivery'))
        
        elif selected_payment_method == 'amar_pay':

            #print("Amar Pay +++++++++++++++", selected_payment_method)
            return HttpResponseRedirect(reverse('initial_payment_amarPay'))
        
        elif selected_payment_method == 'paypal':

            #print("PayPal +++++++++++++++", selected_payment_method)
            return HttpResponse('paypal')
        else:
            print("error in select conditions +++++++++++++++")
    else:
         print("error in POST condition  +++++++++++++++")
