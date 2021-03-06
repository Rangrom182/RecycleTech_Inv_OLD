from django.shortcuts import render
import pandas as pd 
import pandas_highcharts as pdhigh
from django.contrib.auth.decorators import login_required
from django_pandas.io import read_frame
from Inventory.models import Desktop, Laptop, Harddrive, Printer, Item
import json
from django_pandas.io import read_frame
from django.http import JsonResponse

# Create your views here.
@login_required
def dash_index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_desktops = Desktop.objects.all().count()
    num_laptops = Laptop.objects.all().count()
    num_printers = Printer.objects.all().count()
    num_harddrives = Harddrive.objects.all().count()
    num_customers = Desktop.objects.values_list('Transferred_from_Business_Name', flat=True).distinct().order_by().count()
   
    
    context = {
        'num_desktops': num_desktops,
        'num_laptops': num_laptops,
        'num_printers': num_printers,
        'num_harddrives': num_harddrives,
        'num_customers': num_customers
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'dash/dash_index.html', context=context)


# Create your views here.
@login_required
def customer_view(request):
    customers = Desktop.objects.values_list('Transferred_from_Business_Name', flat=True).distinct().order_by()
    context = {
        'customers': customers,
        'header': 'Customers'
    }
    return render(request, "dash/customers.html", context=context)


# def customer_inventory(request, customer):
#     cust_inventory = Item.objects.filter(Transferred_from_Business_Name=customer)
#     context = {
#         'customer_inv': cust_inventory,
#         'header': customer
#     }
#     return render(request, 'customer_inventory.html', context)




