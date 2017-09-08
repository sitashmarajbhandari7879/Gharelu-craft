
from django.conf.urls import url
from .views import profilter

urlpatterns = [
    url(r'^market/', profilter, name='product-filter'),

]