from django.shortcuts import redirect, HttpResponse
from cart.models.wish_list import Wish_List

def delete_wish_list(request,pk):
    delete_item = Wish_List.objects.get(pk=pk).delete()

    return redirect('view_wish_list')