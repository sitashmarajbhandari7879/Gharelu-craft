

from django.shortcuts import render
from product.models import Product
from .filters import ProductFilter

def profilter(request):
    pro_list = Product.objects.all()
    pro_filter = ProductFilter(request.GET, queryset=pro_list)

    return render(request, 'market.html', {'filter': pro_filter})