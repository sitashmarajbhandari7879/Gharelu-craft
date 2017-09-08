


# Create your views here.

from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Product

class ProductListView(ListView):
	model=Product
	template_name='home/market.html'

	def get_context_data(self,**kwargs):
		context=super(ProductListView,self).get_context_data(*kwargs)
		context['product']=Product.objects.all()
		return context


