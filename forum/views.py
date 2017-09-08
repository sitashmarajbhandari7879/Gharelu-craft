
from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from .models import Forum
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse

# Create your views here.
class ForumView(LoginRequiredMixin,CreateView):
	login_url='login'
	template_name='forumform.html'
	model=Forum
	success_url='forum'
	fields='__all__'


class ForumListView(ListView):
	model=Forum
	template_name='forum.html'

	def get_context_data(self,**kwargs):
		context=super(ForumListView,self).get_context_data(*kwargs)
		context['forum']=Forum.objects.all()
		return context

