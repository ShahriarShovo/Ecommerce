from django.shortcuts import render
from cart.models.wish_list import Wish_List


def view_wish_list(request):
    
    get_wish_list = Wish_List.objects.filter(user=request.user, is_added=True,)

    count_wish_list=get_wish_list.count()

    print("Get wish list", get_wish_list)

    context={
        'get_wish_list':get_wish_list,
        'count_wish_list':count_wish_list,
    }

    return render(request,'cart/wish_list.html',context=context)