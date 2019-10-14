from django.conf.urls import url
from .views import *
from .forms import *

urlpatterns = [

    url(r'^$', index_P_D_L, name='index_P_D_L'),
    url(r'^display_desktop$', display_desktops, name="display_desktops"),
    url(r'^display_laptop$', display_laptops, name="display_laptops"),
    url(r'^display_printer$', display_printers, name="display_printers"),
    url(r'^display_hard_drive$', display_hard_drives, name="display_hard_drives"),

    # Add buttons
    url(r'^add_desktop$', add_desktop, name='add_desktop'),
    url(r'^add_laptop$', add_laptop, name='add_laptop'),
    url(r'^add_printer$', add_printer, name='add_printer'),
    url(r'^add_hard_drives$', add_hard_drives, name='add_hard_drives'),

    # Edit buttons
    url(r'^edit_desktop/(?P<pk>\d+)$', edit_desktop, name="edit_desktop"),
    url(r'^edit_laptop/(?P<pk>\d+)$', edit_laptop, name="edit_laptop"),
    url(r'^edit_printer/(?P<pk>\d+)$', edit_printer, name="edit_printer"),
    url(r'^edit_hard_drives/(?P<pk>\d+)$', edit_hard_drives, name="edit_hard_drives"),


    # Delete buttons
    url(r'^delete_desktop/(?P<pk>\d+)$', delete_desktop, name="delete_desktop"),
    url(r'^delete_laptop/(?P<pk>\d+)$', delete_laptop, name="delete_laptop"),
    url(r'^delete_printer/(?P<pk>\d+)$', delete_printer, name="delete_printer"),
    url(r'^delete_hard_drives/(?P<pk>\d+)$', delete_hard_drives, name="delete_hard_drives"),


]
