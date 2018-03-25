from django.db import connection
from django.http import HttpResponse
from django.shortcuts import render

from inventory.models import sells
from items.models import Item
from pharmacy.models import Pharmacy
from customer.models import customer
from cart.models import contains
from customer.models import address_list
from pharmacy.models import contact_pharmacy
item_OTC = []
from cart.views import addItem

def showSearch(request):
    print("hello")
    return render(request,'items/search.html')


def showSearchResult(request):
    name=request.session['name']
    user=customer.objects.get(username=name)
    cart = contains.objects.filter(cart_id=user)
    count = 0
    for cart_id in cart:
        count = count + 1
    print(count)

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
                    print ('loop')
                    print('if')
                    item_OTC .append(a)
                    print (item_OTC)
                else:
                     continue
            print(status)
            return render(request,'items/search_result.html',{'items': item_OTC,'user':user,'items_in_cart':count})

        except:
            print ('except')
            return render(request, 'items/search_result.html', {'user':user,'items_in_cart':count})

    else:
        print ('o else')
        return render(request, 'items/search_result.html', {'user':user,'items_in_cart':count})

def showSearchResultPharmacy(request,item_id):
    name = request.session['name']
    user = customer.objects.get(username=name)
    address_instance = address_list.objects.filter(username=user, default=True).first()
    cart = contains.objects.filter(cart_id=user)
    count = 0
    for cart_id in cart:
        count = count + 1
    print(count)
    set_of_pharmacy = []
    item_info_sells = []
    t=sells.objects.filter(item_id=item_id)
    item=Item.objects.get(item_id=item_id)
    cursor=connection.cursor()
    cursor.execute("SELECT * FROM pharmacy_Pharmacy m INNER JOIN inventory_sells s on m.pharmacy_id=s.pharmacy_id_id JOIN pharmacy_contact_pharmacy p on m.pharmacy_id=p.pharmacy_id  where p.default=true and s.item_id_id=%s", [item_id])
    for row in cursor.fetchall():
        if row[10]-address_instance.address_pincode<=3 and row[13]>0:
            set_of_pharmacy.append(row)
    print (set_of_pharmacy)
    context={'item':item,'pharmacy':set_of_pharmacy,'user':user,'items_in_cart':count}

    return render(request,'items/pharmacy_having_item.html',context=context)

