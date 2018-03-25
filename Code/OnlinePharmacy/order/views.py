from django.http import HttpResponse
from django.shortcuts import render
from notifications.models import notifications_to_pharmacy
from pharmacy.models import Pharmacy
from customer.models import customer
from prescription.models import Prescription
from cart.models import contains
from customer.models import address_list

from pharmacy.forms import PrescriptionForm
def orderPlaced(request):
    return HttpResponse('<h1> Your order with <order id> is placed. </h1>')

def addressPage(request):
    return HttpResponse('<h1> Page asking for address for delievery. </h1>')

def choicePage(request):
    return HttpResponse('<h1> Choices are given on this page </h1>')

def prescriptionPage(request):
    name = request.session['name']
    user_name = customer.objects.get(username=name)
    cart = contains.objects.filter(cart_id=user_name.cart_id)
    count = 0
    for cart_id in cart:
        count = count + 1
    print(count)
    #form = PrescriptionForm(request.POST or None, request.FILES or None)
    if request.method == 'POST':
        prescription=Prescription()
        img=request.POST.get('file')
        print(img)
        prescription.prescription_image=img
        user = customer()
        user.username = request.session['name']
        prescription.uploaded_by = user
        prescription.flag_for_fulfillment = "False"
        print('form aane vala hai!!')

        prescription.save()

        create_noti(request,prescription.prescription_id)
        return HttpResponse('Done')


    return render(request,'order/prescription_upload1.html',{'user':user_name,'items_in_cart':count})

def create_noti(request,id):
    print(id)
    print('function')
    user = request.session['name']
    user_name = customer.objects.get(username=user)
    address_instance = address_list.objects.filter(username=user,default=True).first()
    print(address_instance.address_pincode)
    print (user)
    set_of_pharmacies = []
    pharmacies=Pharmacy.objects.all()
    for ph in pharmacies:
        print(ph.address_pincode)
        if ph.address_pincode-address_instance.address_pincode <= 3:
            set_of_pharmacies.append(ph)

    customer_sending = customer()
    customer_sending.username=user
    print(set_of_pharmacies)
    pres = Prescription.objects.get(prescription_id=id)
    print(pres.prescription_id)
    for b in set_of_pharmacies:
         print('loop')
         print(b)
         notification = notifications_to_pharmacy()
         phar=Pharmacy()
         phar.pharmacy_id=b.pharmacy_id
         notification.pharmacy_id=phar
         notification.content="hii"
         notification.sent_by_customer_id = customer_sending.username
         a=Prescription()
         a.prescription_id=pres.prescription_id
         print(a)
         notification.prescription_id=a
         notification.prescription_image=pres.prescription_image

         notification.save()

def prescriptionPage1(request):
    name = request.session['name']
    user = customer.objects.get(username=name)
    cart = contains.objects.filter(cart_id=user.cart_id)
    if request.method == "POST":
        img=request.POST.get('file')
        print (img)
    count = 0
    for cart_id in cart:
        count = count + 1
    print(count)
    return render(request, 'order/prescription_upload2.html',{'user': user, 'items_in_cart': count})