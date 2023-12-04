from django.shortcuts import render, HttpResponse
from products.models.products_model import Products
from user_auth.models.user import User
from orders.models.orders import Order
from cart.models.cart import Cart

# Create your views here.

def admin_home(reques):
    lebel=[]
    data =[]
    total_product= Products.objects.count()
    total_user = User.objects.count()
    todays_order = Cart.objects.filter(select_order_stats=1).count()
    total_cart = Cart.objects.count()
    print("todays_order ---------------",todays_order)
    return render(reques, 'admin/dashboard/admin_dashboard.html', locals())