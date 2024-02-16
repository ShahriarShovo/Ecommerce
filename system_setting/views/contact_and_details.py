from django.shortcuts import render
from system_setting.models.contact import Contact
from products.models.products_model import Products

def contact_and_details(request):
    get_contact = Contact.objects.first()

    get_product = Products.objects.all()[:4]
    
    # context={
    #     'get_product':get_product,
    #     'get_contact': get_contact
    # }

    print(get_contact)
    return {'get_contact': get_contact, 'get_product':get_product,}