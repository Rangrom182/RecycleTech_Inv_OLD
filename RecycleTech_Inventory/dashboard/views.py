from django.shortcuts import render
import pandas as pd 
import pandas_highcharts as pdhigh
from django.contrib.auth.decorators import login_required
from django_pandas.io import read_frame
from Inventory.models import Desktop, Laptop, Harddrive, Printer
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
    
    context = {
        'num_desktops': num_desktops,
        'num_laptops': num_laptops,
        'num_printers': num_printers,
        'num_harddrives': num_harddrives,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'dash/dash_index.html', context=context)




