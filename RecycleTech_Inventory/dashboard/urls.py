from django.urls import path
from django.conf.urls import url
from dashboard import views as dash_views

from .forms import *

urlpatterns = [

    path('', dash_views.dash_index, name='dash_index'),
    path('customers/', dash_views.customer_view, name="customer_view"),
    #path('customer_inventory/', dash_views.customer_inventory, name="customer_inventory")

]