from django.conf.urls import url
from django.views.generic.list import ListView
from .views import ProductListView

urlpatterns=[
	url(r'^product$',ProductListView.as_view(),name="product"),


]
