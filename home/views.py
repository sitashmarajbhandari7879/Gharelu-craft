
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, FormView
from product.models import Product
from .models import Supplier
from django.views.generic.list import ListView

from .supplyforms import SupplierForm


# Create your views here.
def home(request):
	template_name='index.html'
	return render(request,template_name)

class ProductListView(ListView):
	model=Product
	template_name='market.html'

	def get_context_data(self,**kwargs):
		context=super(ProductListView,self).get_context_data(*kwargs)
		context['product']=Product.objects.all()
		return context



def volunteer(request):
	template_name='volunteer1.html'
	return render(request,template_name)

def projects(request):
	template_name='project.html'
	return render(request,template_name)


def training(request):
	template_name='training.html'
	return render(request,template_name)

def contact(request):
	template_name='contact.html'
	return render(request,template_name)

class Knitting(TemplateView):
	template_name = 'project-knitting1.html'

	def get_context_data(self, **kwargs):
		context = super(Knitting, self).get_context_data(**kwargs)
		context['supplier'] = Supplier.objects.all()[:3]
		return context


class SupplierFormView(FormView):
	form_class = SupplierForm
	# model = Contact
	initial = {'key': 'value'}
	template_name = 'supplier_form.html'
	success_url = '/thanks/'

	def get(self, request, *args, **kwargs):
		form = self.form_class(initial=self.initial)
		return render(request, self.template_name, {'form': form})


	def post(self, request, *args, **kwargs):
		form = self.form_class(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return redirect('market')
		return render(request, self.template_name, {'form': form})


class ContactSupplier(TemplateView):
	template_name = 'contact-supplier/contactsupplier.html'

	def get_context_data(self, **kwargs):
		context = super(ContactSupplier, self).get_context_data(**kwargs)
		context['supplier'] = Supplier.objects.all()[:1]
		return context

def trainingdetail(request):
	return render (request, 'train_detail.html')

