from django.shortcuts import render, HttpResponse
from products.models.models import Products

# Create your views here.

def admin_home(reques):
    all_product= Products.objects.all()
    return render(reques, 'admin/dashboard/admin_dashboard.html', locals())
