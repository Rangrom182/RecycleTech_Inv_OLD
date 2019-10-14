from django.shortcuts import render, redirect, get_object_or_404
from .models import Desktop, Laptop, Harddrive, Printer, Item
from .forms import *
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib import messages

# Create your views here.

def invbase(request):
    return render(request, 'invbase.html')

def index_Table_Navbar(request):
    return render(request, 'index_Table_Navbar.html')

def index_HDD(request):
    return render(request, 'index_HDD.html')

@login_required
def index_P_D_L(request):
    return render(request, 'index_P_D_L.html')

# =======================================================================
#                        Display Items
# =======================================================================

def display_desktops(request):
    items = Desktop.objects.all()
    context = {
        'items' : items,
        'header' : 'Desktops'

    }
    return render(request, 'index_P_D_L.html', context)

def display_laptops(request):
    items = Laptop.objects.all()
    context = {
        'items' : items,
        'header': 'Laptops'
    }

    return render(request, 'index_P_D_L.html', context)


def display_printers(request):
    items = Printer.objects.all()
    context = {
        'items': items,
        'header': 'Printers'
    }

    return render(request, 'index_P_D_L.html', context)

def display_hard_drives(request):
    items = Harddrive.objects.all()
    context = {
        'items': items,
        'header': 'Hard Drives'
    }

    return render(request, 'index_HDD.html', context)

# =======================================================================
#                           Add Items
# =======================================================================

def add_item(request, cls, page_redirect):
    if request.method == "POST":
        form = cls(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, f'You have successfully added a new item!')
            return redirect(page_redirect)
    else:
        form = cls()
        return render(request, 'add_new.html', {'form' : form})

def add_laptop(request):
    return add_item(request, LaptopForm, display_laptops)

def add_desktop(request):
    return add_item(request, DesktopForm, display_desktops)

def add_printer(request):
    return add_item(request, PrinterForm, display_printers)

def add_hard_drives(request):
    if request.method == "POST":
        form = HarddriveForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, f'You have successfully added a new item!')
            return redirect('index_HDD')

    else:
        form = HarddriveForm()
        return render(request, 'add_new.html', {'form': form})

# =======================================================================
#                        Edit Items
# =======================================================================

def edit_item(request, pk, model, cls):
    item = get_object_or_404(model, pk=pk)

    if request.method == "POST":
        form = cls(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('index_P_D_L')
    else:
        form = cls(instance=item)

        return render(request, 'edit_item.html', {'form': form})

def edit_desktop(request, pk):
    return edit_item(request, pk, Desktop, DesktopForm)

def edit_laptop(request, pk):
    return edit_item(request, pk, Laptop, LaptopForm)

def edit_printer(request, pk):
    return edit_item(request, pk, Printer, PrinterForm)


def edit_hard_drives(request, pk, model, cls):
    item = get_object_or_404(model, pk=pk)

    if request.method == "POST":
        form = cls(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('index_HDD')
    else:
        form = cls(instance=item)

        return render(request, 'edit_item.html', {'form': form})


# =======================================================================
#                        Delete Items
# =======================================================================

def delete_desktop(request, pk):
    Desktop.objects.filter(id=pk).delete()

    items = Desktop.objects.all()
    context = {
        'items' : items
    }
    messages.success(request, f'You have successfully deleted Desktop Item with ID of {pk}')
    return render(request, 'index_P_D_L.html', context)


def delete_laptop(request, pk):
    Laptop.objects.filter(id=pk).delete()

    items = Laptop.objects.all()
    context = {
        'items' : items
    }
    messages.success(request, f'You have successfully deleted Laptop Item with ID of {pk}')
    return render(request, 'index_P_D_L.html', context)


def delete_printer(request, pk):
    Printer.objects.filter(id=pk).delete()

    items = Printer.objects.all()
    context = {
        'items' : items
    }
    messages.success(request, f'You have successfully deleted Printer Item with ID of {pk}')
    return render(request, 'index_P_D_L.html', context)


def delete_hard_drives(request, pk):
    Harddrive.objects.filter(id=pk).delete()

    items = Harddrive.objects.all()
    context = {
        'items': items
    }
    messages.success(request, f'You have successfully deleted Harddrive Item with ID of {pk}')
    return render(request, 'index_HDD.html', context)




