from django.shortcuts import render
import pandas as pd 
from django.contrib.auth.decorators import login_required
from django_pandas.io import read_frame
from Inventory.models import Desktop, Laptop, Harddrive, Printer, Item
import json
from django.http import JsonResponse

# Create your views here.
@login_required
def dash_index(request):
    df = pd.read_csv("dashboard/data/car_sales.csv")
    rs = df.groupby("Engine size")["Sales in thousands"].agg("sum")
    categories = list(rs.index)
    values = list(rs.values)

    table_content = df.to_html(index=None)
    table_content = table_content.replace("","")
    table_content = table_content.replace('class="dataframe"',"class='table table-striped'")
    table_content = table_content.replace('border="1"',"")

    context = {"categories": categories, 'values': values, 'table_data':table_content}
    return render(request, 'dash/dash_index.html', context=context)


