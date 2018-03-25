from django.db import connection
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from customer.models import customer
from items.models import Item
from cart.models import contains
from pharmacy.models import Pharmacy
from inventory.models import sells
from order.models import orderOTC
from customer.models import address_list



def showCart(request):
    item_table = []
    a = 1
    sum=0
    name=request.session['name']
    user=customer.objects.get(username=name)
    cart = contains.objects.filter(cart_id_id=user)
    count = 0
    for cart_id in cart:
        count = count + 1
    print(count)

    cursor = connection.cursor()
    cursor.execute(
        "SELECT * FROM inventory_sells m INNER JOIN cart_contains s on m.id=s.product_id_id INNER JOIN items_Item i on m.item_id_id =i.item_id where s.cart_id_id=%s",
        [request.session['name']])
    for row in cursor.fetchall():
        item_table.append(row)
        sum=sum+row[2]*row[6]
    print (item_table)
    print(sum)
    context = {'item':item_table,'user':user,'items_in_cart':count,'i':a,'totalCost':sum}
    return render(request,'cart/cart.html',context)



def createCart(username):
    latest = customer.objects.order_by('-cart_id')[0].cart_id
    currentUser = customer.objects.filter(username=username).first()
    if latest == 0:
        currentUser.cart_id = 100000
    else :
        currentUser.cart_id = latest+1
    currentUser.save()



def addItem(request,item_id):
    item_instance = Item.objects.get(item_id=item_id)
    user_instance = customer.objects.get(username=request.session['name'])
    sells_instance=sells.objects.filter(item_id_id=item_id).first()
    instance = contains.objects.filter(cart_id=user_instance.cart_id,product_id=sells_instance.id).first()
    if instance :
        instance.quantity = instance.quantity + 1
        instance.update()

    else :
        instance = contains()
        instance.cart_id = user_instance
        instance.product_id = sells_instance
        instance.quantity = 1
        instance.save()
    return HttpResponseRedirect('http://localhost:8000/search/result/')



def deleteItem(request,item_id,pharmacy_id):
    user_instance = customer.objects.get(username=request.session['name'])
    product_instance=sells.objects.get(item_id_id=item_id,pharmacy_id_id=pharmacy_id)
    instance = contains.objects.filter(cart_id_id=user_instance.username,product_id_id=product_instance.id).delete()
    return HttpResponse('<h1> The item is deleted from cart. </h1>')



def emptyCart(request):

    user_instance = customer.objects.get(username=request.session['name'])
    instance = contains.objects.get(cart_id=user_instance).delete()

    return HttpResponse('<h1>The cart is empyted successfully. </h1>')

def updateCart(request,id):
    item_table = []
    name = request.session['name']
    user = customer.objects.get(username=name)
    cart = contains.objects.filter(cart_id_id=user)
    count = 0
    for cart_id in cart:
        count = count + 1
    print(count)

    cursor = connection.cursor()
    cursor.execute(
        "SELECT * FROM inventory_sells m INNER JOIN cart_contains s on m.id=s.product_id_id INNER JOIN items_Item i on m.item_id_id =i.item_id where s.cart_id_id=%s",
        [request.session['name']])
    for row in cursor.fetchall():
        item_table.append(row)
    print(item_table)
    instance = contains.objects.get(id=id)
    instance.quantity=instance.quantity+1
    instance.save()
    context = {'item': item_table, 'user': user, 'items_in_cart': count}
    return render(request, 'cart/cart.html', context)


def addItemByParticularPharmacy(request,pharmacy_id,item_id):
    name = request.session['name']
    user = customer.objects.get(username=name)
    cart = contains.objects.filter(cart_id_id=user)
    count = 0
    for cart_id in cart:
        count = count + 1
    print(count)
    sells_instance = sells.objects.get(item_id_id=item_id,pharmacy_id_id=pharmacy_id)
    instance = contains()
    instance.cart_id = user
    instance.product_id = sells_instance
    instance.quantity = 1
    instance.save()


    return HttpResponseRedirect('http://localhost:8000/search/result/')

def itemCheckout(request,id):
    name = request.session['name']
    user = customer.objects.get(username=name)
    cart = contains.objects.filter(cart_id_id=user)
    count = 0
    for cart_id in cart:
        count = count + 1
    print(count)
    product_instance=sells.objects.get(id=id)
    product_instance.quantity=product_instance.quantity-1
    orderId=create_orderOTC_id(request)
    create_order(request,orderId,id)
    instance = contains.objects.filter(cart_id_id=user.username, product_id_id=id).delete()

    return HttpResponse('done!')


def create_order(request,orderid,product_id):
        order_final=orderOTC()
        product=sells()
        product.id=product_id
        order_final.product_id=product
        order_final.order_id=orderid
        #order_final.order_date= "2018-09-09"
        order_final.delivered_date = "2018-09-09"
        u = customer()
        u.username=request.session['name']
        order_final.buyer=u#to be taken from form
        address_instance= address_list.objects.filter(username=order_final.buyer,default=True).first()
        order_final.address_street=address_instance.address_street
        order_final.address_pincode=address_instance.address_pincode
        order_final.address_state=address_instance.address_state
        order_final.address_city=address_instance.address_city
        order_final.save()



def create_orderOTC_id(request):
    name = request.session['name']
    latest = orderOTC.objects.all()
    orderid = 800000
    if not latest :
       orderid = 800000
    else:
        orderid = orderid + 1

    return orderid