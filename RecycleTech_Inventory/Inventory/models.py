from django.db import models

# Create your models here.
class Item(models.Model): # Name of the table
    Item_Name                       = models.CharField(max_length=120, blank=False)
    Serial                          = models.CharField(max_length=120)
    Transferred_from_Business_Name  = models.CharField(max_length=120, default="Enter Business Name")
    HDD_Disposed                    = models.CharField(max_length=20, default="None", choices=[('None', 'No'),('Yes Disposed', 'Yes'),('Not Disposed', 'No')])
    HDD_DOD_Wiped                   = models.CharField(max_length=20, default="None", choices=[('None', 'No'),('Yes Wiped', 'Yes'),('Not Wiped', 'No')])
    Refurbish_Status                = models.CharField(max_length=20, default="None", choices=[('None', 'Status'),('Not Finished', 'Not Complete'),('Partially Done', 'Partial Completion'), ('Finished', 'Complete')])
    SSD_Size                        = models.CharField(max_length=120, default="SSD Size")
    SSD_Replacement_Price           = models.DecimalField(max_digits=1000, decimal_places=2)
    Ram_QTY                         = models.CharField(choices=[('None', 'No Ram installed'), ('2GB', '2GB installed'), ('4GB', '4GB Installed'), ('8GB', '8GB Installed'), ('16GB', '16GB Installed')], max_length=120, default="None")
    Processor                       = models.CharField(max_length=10, default="Type", choices=[('Type','Processor Type'),('Core 2 Duo', "Core 2 Duo"), ('Core i3', 'Core i3'), ('Core i5', 'Core i5'), ('Core i7', 'Core i7')])
    Price                           = models.DecimalField(max_digits=1000, decimal_places=2, null=True, blank=True)
    Sold_To                         = models.CharField(max_length=120, null=True, blank=True)
    Paid                            = models.CharField(max_length=120, default="None", choices=[('None', 'No'),('Yes Paid', 'Yes'),('Not Paid', 'No')])
    Invoice_Num                     = models.IntegerField(null=True, blank=True)

    class Meta:
        abstract = False

    def __str__(self):
        return('Model: {0}. \n' 
        'Refurbish Status: {1}. \n' 
        'Sold To: {2}.'.format(self.Item_Name, self.Refurbish_Status, self.Sold_To))

class Laptop(Item): # Name of the table
    pass

class Desktop(Item): # Name of the table
    pass

class Printer(Item):  # Name of the table
    pass

class Harddrive(models.Model):
    Serial           = models.IntegerField()
    Size             = models.CharField(max_length=120, default="Enter Size")
    Pulled_From      = models.CharField(max_length=120, blank=False)
    Computer_Serial  = models.IntegerField()
    Business_Name    = models.CharField(max_length=120, default="Enter business Name")
    DOD_Wiped        = models.CharField(max_length=20, default="None", choices=[('None', 'No'),('Yes Wiped', 'Yes'),('Not Wiped', 'No')])
    Disposed         = models.CharField(max_length=20, default="None", choices=[('None', 'No'),('Yes Disposed', 'Yes'),('Not Disposed', 'No')])
    Reused           = models.CharField(max_length=20, default="Pick One", choices=[('Pick One', 'Pick'), ("Yes Reused", 'Yes'), ("Not Reused", 'No')])

    def __str__(self):
        return('Serial: {0}. \n Size: {1} \n Pulled_From: {2} \n'
               'Disposed: {3}'.format(self.Serial, self.Size, self.Pulled_From, self.Disposed))


