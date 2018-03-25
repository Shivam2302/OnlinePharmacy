from datetime import timezone

from django.db import connection
from django.http import HttpResponse, HttpResponseRedirect
from django.apps import apps
from django.shortcuts import render, redirect
from django.views import View

from django.apps import apps
from items.models import Item
from inventory.models import sells
from pharmacy.models import Pharmacy
from online_pharmacy import settings

from inventory.forms import InventoryForm
from inventory.forms import SellsForm

def showInventory(request):
    pharmacy = request.session['name']
    pharmacy_info = Pharmacy.objects.get(pharmacy_id=pharmacy)
    items_i=sells.objects.filter(pharmacy_id=pharmacy)
    set_of_items = []
    cursor = connection.cursor()
    cursor.execute(
        "SELECT * FROM inventory_sells m INNER JOIN items_Item s on m.item_id_id=s.item_id where m.pharmacy_id_id=%s",
        [pharmacy])
    for row in cursor.fetchall():
            set_of_items.append(row)
    print(set_of_items)
    return render(request, 'inventory/inventory.html', {'item':set_of_items,'pharmacy':pharmacy_info})



#def addItemInInventory(request):
    #items=Item.objects.all()
    #print(request.session['name'])
    #return render(request,'inventory/create.html',{'items':items})

def addItemInInventory(request):
    pharmacy=request.session['name']
    pharmacy_info=Pharmacy.objects.get(pharmacy_id=pharmacy)
    return render(request,'inventory/create.html',{'pharmacy':pharmacy_info})

def addItemInInventoryResult(request):
    pharmacy = request.session['name']
    pharmacy_info = Pharmacy.objects.get(pharmacy_id=pharmacy)
    print(request)
    if request.method == 'POST':
        print('request')
        itemname = request.POST.get('search')
        try:
            status = Item.objects.filter(item_name__icontains=itemname)
            print('hi')
            print(status)
            for a in status:

                if a.otc_or_not is True:
                    print('loop')
                    print('if')
                    item_OTC = a
                    print(item_OTC)
                else:
                    continue
            print(status)
            return render(request, 'inventory/search_result.html', {'items': status,'pharmacy':pharmacy_info})

        except:
            print('except')
            return render(request, 'inventory/search_result.html', {'pharmacy':pharmacy_info})

    else:
        print('o else')
        return render(request, 'inventory/search_result.html',{'pharmacy':pharmacy_info})


def createInventory1(request,item_id):
    pharmacy = request.session['name']
    pharmacy_info = Pharmacy.objects.get(pharmacy_id=pharmacy)
    form1=SellsForm()
    #form1.item_id=item_id
    s=Item.objects.get(item_id=item_id)
    if request.method == 'POST':
        form1 = SellsForm(request.POST, request.FILES)
        if form1.is_valid():
            info=form1.save(commit=False)
            print(item_id)
            temp = Item()
            temp.item_id = item_id
            info.item_id = temp
            print(info.item_id)
            temp1 = Pharmacy()
            temp1.pharmacy_id = request.session['name']
            print(temp1.pharmacy_id)
            info.pharmacy_id=temp1
            info.save()

            return HttpResponseRedirect('/pharmacy_name/inventory/show/')



        else:
            return render(request, 'inventory/create_inventory.html', {'form1':form1,'item':s,'pharmacy':pharmacy_info})
    else:
        return render(request, 'inventory/create_inventory.html', {'form1': form1,'item':s,'pharmacy':pharmacy_info})


def addNewProduct(request):#(add new product)
    print(request.method)
    form=InventoryForm()


    if request.method == 'POST':
        form = InventoryForm(request.POST, request.FILES)


        if form.is_valid() :
             print("form")
             information = form.save(commit=False)

             information.save()


             render(request,'inventory/create.html')
        else:
            form = InventoryForm()


            context = {
            'form': form,
            }
            return render(request, 'inventory/add_new_product.html.html', context=context)

    else:
         return render(request, 'inventory/add_new_product.html',{'form':form} )

