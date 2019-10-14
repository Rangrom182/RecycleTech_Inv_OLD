# Bring in the Django.forms
from django import forms
from .models import Item, Laptop, Desktop, Harddrive, Printer

class LaptopForm(forms.ModelForm):
    class Meta:
        model = Laptop
        fields = ('Item_Name', 'Serial', 'Transferred_from_Business_Name',
                  'HDD_Disposed', 'HDD_DOD_Wiped', 'Refurbish_Status',
                  'SSD_Size', 'SSD_Replacement_Price',
                  'Ram_QTY', 'Processor', 'Price', 'Sold_To',
                  'Paid', 'Invoice_Num')


class DesktopForm(forms.ModelForm):
    class Meta:
        model = Desktop
        fields = ('Item_Name', 'Serial', 'Transferred_from_Business_Name',
                  'HDD_Disposed', 'HDD_DOD_Wiped', 'Refurbish_Status',
                  'SSD_Size', 'SSD_Replacement_Price',
                  'Ram_QTY', 'Processor', 'Price', 'Sold_To',
                  'Paid', 'Invoice_Num')



class PrinterForm(forms.ModelForm):
    class Meta: 
        model = Printer
        fields = ('Item_Name', 'Serial', 'Transferred_from_Business_Name',
                  'HDD_Disposed', 'HDD_DOD_Wiped', 'Refurbish_Status',
                  'SSD_Size', 'SSD_Replacement_Price',
                  'Ram_QTY', 'Processor', 'Price', 'Sold_To',
                  'Paid', 'Invoice_Num')

class HarddriveForm(forms.ModelForm):
    class Meta:
        model = Harddrive
        fields = ('Serial', 'Size', 'Pulled_From', 'Computer_Serial',
                    'Business_Name', 'DOD_Wiped', 'Disposed', 'Reused' )

