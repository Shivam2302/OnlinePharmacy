from datetime import datetime

from django.contrib.auth import authenticate
from django.db import connection
from django.http import HttpResponse, HttpResponseRedirect
from django.apps import apps
from django.shortcuts import render
from notifications.models import notifications_to_pharmacy
from pharmacy.models import Pharmacy
from notifications.models import Notifications_to_user
from order.models import order
from customer.models import address_list
from customer.models import customer
from prescription.models import Prescription
from customer.models import address_list
from pharmacy.models import contact_pharmacy
from cart.models import contains


def showDashboard2(request):
    name = request.session['name']
    pharmacy_info=Pharmacy.objects.get(pharmacy_id=name)
    return render(request,"pharmacy/dashboard.html",{'pharmacy':pharmacy_info})

def showNotifications(request):
        phar = request.session["name"]
        pharmacy_info = Pharmacy.objects.get(pharmacy_id=phar)
        notifications_fulfilled = []
        notifications_notfulfilled = []
        print(phar)
        notification = notifications_to_pharmacy.objects.filter(pharmacy_id_id=phar)
        for a in notification:
             print(a.prescription_id_id)
             prescription_info=Prescription.objects.get(prescription_id=a.prescription_id_id)
             print(prescription_info.prescription_id)
             print(prescription_info.flag_for_fulfillment)
             if prescription_info.flag_for_fulfillment == True:
                 notifications_fulfilled.append(a)
             elif prescription_info.flag_for_fulfillment == False:
                 notifications_notfulfilled.append(a)
        print(notifications_fulfilled)
        print('gap')
        print(notifications_notfulfilled)
        return render(request,"pharmacy/notification.html",{'notifications_fulfilled': notifications_fulfilled,'pharmacy':pharmacy_info,'notifications_notfulfilled': notifications_notfulfilled})

def acceptNotification(request,prescription_id):
        if request.method == "POST":
                print('accept')
                print(prescription_id)
                pres = Prescription.objects.get(prescription_id=prescription_id)
                print(pres.flag_for_fulfillment)
                print(pres.uploaded_by_id)
                if pres.flag_for_fulfillment == False:
                        orderid=create_order_id(request)
                        create_noti_to_user(request,prescription_id,orderid)
                        create_order(request,prescription_id,orderid)
                        pres.flag_for_fulfillment = True
                        pres.save()
                        return HttpResponseRedirect('/pharmacy_name/notifications')
                else:
                    return HttpResponse('flagggg')
        else:
                return HttpResponse('sorry')

def create_noti_to_user(request,id,orderid):
                phar = request.session["name"]
                pharmacy_info = Pharmacy.objects.get(pharmacy_id=phar)
                print('function_executed1')
                pres = Prescription.objects.get(prescription_id=id)
                print(pres.uploaded_by)
                notification = Notifications_to_user()#pass data from html file to here
                u=customer()
                u.username=pres.uploaded_by_id
                notification.username_reciever = u
                notification.content= "your order has been confirmed with order id " + str(orderid)+" by the pharmacy " + str(pharmacy_info)
                phar=Pharmacy()
                phar.pharmacy_id=request.session['name']
                notification.sent_by_pharmacy=phar
                notification.save()


def create_order(request,id,orderid):
        order_final=order()
        phar = Pharmacy()
        phar.pharmacy_id = request.session['name']
        order_final.pharmacy_id= phar
        order_final.order_id=orderid
        #order_final.order_date= "2018-09-09"
        order_final.delivered_date = "2018-09-09"
        pres = Prescription.objects.get(prescription_id=id)
        order_final.pres_id = pres
        u = customer()
        u.username = pres.uploaded_by_id
        order_final.buyer=u#to be taken from form
        address_instance=address_list.objects.filter(username=order_final.buyer,default=True).first()
        order_final.address_street=address_instance.address_street
        order_final.address_pincode=address_instance.address_pincode
        order_final.address_state=address_instance.address_state
        order_final.address_city=address_instance.address_city
        order_final.save()

def pharmacy_detail(request,pharmacy_id):
    name = request.session['name']
    user=customer.objects.get(username=name)
    print(user.cart_id)
    cart = contains.objects.filter(cart_id_id=user)
    count = 0
    for cart_id in cart:
        count = count + 1
    print(count)
    pharmacy_info=[]

    cursor = connection.cursor()
    cursor.execute(
        "SELECT * FROM pharmacy_Pharmacy m INNER JOIN pharmacy_contact_pharmacy s on m.pharmacy_id=s.pharmacy_id where s.default=true and m.pharmacy_id=%s",
        [pharmacy_id])
    for row in cursor.fetchall():
        pharmacy_info.append(row)
    print( pharmacy_info)
    return render(request,'pharmacy/detail.html',{'pharmacy':pharmacy_info,'user':user,'items_in_cart':count})

def p_logout(request):
    del request.session['name']
    return HttpResponseRedirect('/pharmacy/login')

def create_order_id(request):
    name = request.session['name']
    latest = order.objects.all()
    orderid = 200000
    if not latest :
       orderid = 200000
    else:
        orderid = orderid + 1

    return orderid