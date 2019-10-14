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
    qs = Desktop.objects.all()
    df = read_frame(qs, fieldnames=['Item_Name', 'Transferred_from_Business_Name'])
    df['Item_Name'] = df['county'].map(df['county'].value_counts())
    rs = df.groupby("Transferred_from_Business_Name")["Item_Name"].agg("sum")
    categories = list(rs.index)
    values = list(rs.values)

    table_content = df.to_html(index=None)
    table_content = table_content.replace("","")
    table_content = table_content.replace('class="dataframe"',"class='table table-striped'")
    table_content = table_content.replace('border="1"',"")

    context = {"categories": categories, 'values': values, 'table_data':table_content}
    return render(request, 'dash/dash_index.html', context=context)




