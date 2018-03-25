from django.contrib.auth import authenticate
from django.http import HttpResponse, HttpResponseRedirect
from django.apps import apps
from django.shortcuts import render
from .models import contact_customer
from Register_and_login.forms import UserContact

from cart.models import contains
from .models import customer
from order.models import order
from notifications.models import Notifications_to_user
from customer.models import address_list

from customer.forms import customerForm
def showHomepage1(request):
    name = request.session['name']
    user = customer.objects.get(username=name)
    print (user.cart_id)
    cart = contains.objects.filter(cart_id_id=user)
    count = 0
    for cart_id in cart:
        count=count+1
    print (count)
    return render(request,'customer/homepage.html',{'user':user,'items_in_cart':count})

def showDashboard1(request):
    name=request.session['name']
    user=customer.objects.get(username=name)
    #same above cart thing has to be done in this
    form = customerForm(request.POST or None)
    cart = contains.objects.filter(cart_id_id=user)
    count = 0
    for cart_id in cart:
        count = count + 1
    print(count)
    return render(request, 'customer/dashboard.html',{'user':user,'items_in_cart':count,'form':form})

def dropdown(request):
    return render(request, 'customer/dropdown.html')

def logout(request):
    del request.session['name']
    return HttpResponseRedirect('/user/login')

def address_log(request):
    name = request.session['name']
    user = customer.objects.get(username=name)
    cart = contains.objects.filter(cart_id_id=user)
    count = 0
    for cart_id in cart:
        count = count + 1
    print(count)
    addresslist=address_list.objects.filter(username=name)
    return render(request, 'customer/address_log.html', {'user': user,'items_in_cart':count,'addresslist':addresslist})

def order_log(request):
    name = request.session['name']
    user = customer.objects.get(username=name)
    cart = contains.objects.filter(cart_id_id=user)
    count = 0
    for cart_id in cart:
        count = count + 1
    print(count)
    #order_list = order.objects.filter(buyer=name)
    #return render(request, 'customer/order_log.html', {'user': user,'order_list' :order_list})
    return render(request, 'customer/order_log.html', {'user': user,'items_in_cart':count})

def showNotifications(request):
    name = request.session['name']
    user = customer.objects.get(username=name)
    cart = contains.objects.filter(cart_id_id=user)
    count = 0
    for cart_id in cart:
        count = count + 1
    print(count)
    notification_list=Notifications_to_user.objects.filter(username_reciever=name)
    return render(request, 'customer/notification.html',{'user':user,'notification_list':notification_list,'items_in_cart':count})

def saveChanges(request):

        username=request.GET['Username']

        print(username)
        return HttpResponseRedirect('/username/dashboard')

def deleteAddress(request, id):

    name=request.session['name']
    addresslog=address_list.objects.get(username=name,id=id).delete()
    return HttpResponseRedirect('/username/dashboard/addresslog/')


def user_contact(request):
    form = UserContact(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            number = form.cleaned_data['contact_no']
            alternate = form.cleaned_data['alternate_no']
            street = form.cleaned_data['address_street']
            city = form.cleaned_data['address_city']
            state = form.cleaned_data['address_state']
            pincode = form.cleaned_data['address_pincode']

            user=customer.objects.get(username=request.session['name'])
            print(user.username)

            inst = contact_customer()
            inst.username = user
            inst.contact_no = number
            inst.save()

            inst1 = contact_customer()
            inst1.username = user
            inst1.contact_no = alternate
            inst1.save()

            inst = address_list()
            first_address = address_list.objects.filter(username=user).first()
            if not first_address:
                inst.default = "True"

            inst.username = user
            inst.address_street = street
            inst.address_city = city
            inst.address_state = state
            inst.address_pincode = pincode
            inst.save()

            return HttpResponseRedirect('/username/dashboard/addresslog')

    return render(request, 'customer/userAddress.html', context={'form': form})