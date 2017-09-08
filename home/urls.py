
from django.conf.urls import url
from .views import (ProductListView,volunteer,home,contact,projects,Knitting,
SupplierFormView, ContactSupplier,training,trainingdetail)



urlpatterns = [
	url(r'^$',home, name='home'),
    url(r'^market/$',ProductListView.as_view(), name='market'),
    
    url(r'^volunteer/$',volunteer, name='volunteer'),
    url(r'^training/$',training, name='training'),
    url(r'^project/$',projects, name='project'),
    url(r'^contact/$',contact, name='contact'),
    url(r'^train/$',trainingdetail, name='train'),
    url(r'^knitting/$',Knitting.as_view(), name='knitting'),
	url(r'^supplier-form/$', SupplierFormView.as_view(), name='supplier-form'),
    url(r'^contact-supplier/$', ContactSupplier.as_view(), name='contact-supplier'),

]

