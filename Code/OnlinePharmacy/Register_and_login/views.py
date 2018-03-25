from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from .forms import PharmacyRegistration,CustomerRegistration,CustomerLogin,PharmacyLogin
from django.contrib import messages
from customer.models import customer
from pharmacy.models import Pharmacy
from cart.views import createCart
from Register_and_login.forms import PharmacyContact
from Register_and_login.forms import UserContact
from pharmacy.models import contact_pharmacy
from customer.models import contact_customer
from customer.models import address_list


def index(request):
    return render(request,'Register_and_login/index.html')


def user_registration(request):
    form = CustomerRegistration(request.POST or None, request.FILES or None)
    if request.method == 'POST':
        if form.is_valid():
            information = form.save(commit=False)
            information.save()
            request.session['user'] = information.username
            createCart(form.cleaned_data['username'])
            return HttpResponseRedirect('/user/contact')
    return render(request, 'Register_and_login/userRegistration.html', context={'form': form})


def pharmacy_registration(request):
    form = PharmacyRegistration(request.POST or None, request.FILES or None)
    print(request.FILES)
    if request.method == 'POST':
        if form.is_valid():
            information = form.save(commit=False)
            information.save()
            request.session['pharmacy'] = information.pharmacy_id
            return HttpResponseRedirect('/pharmacy/contact')
    return render(request, 'Register_and_login/pharmacyRegistration.html', context={'form': form})



def user_login(request):
    form = CustomerLogin(request.POST or None, request.FILES or None)
    if request.method == 'POST':
        if form.is_valid():
            user = form.cleaned_data['username']
            pas = form.cleaned_data['password']
            cust = customer.objects.filter(username=user,password=pas)
            request.session['name'] = user
            if cust:
                return HttpResponseRedirect('/homepage')
            else:
                messages.error(request,'Invalid username or password')

    return render(request, 'Register_and_login/userLogin.html', context={'form': form})


def pharmacy_login(request):
    form = PharmacyLogin(request.POST or None, request.FILES or None)
    if request.method == 'POST':
        if form.is_valid():
            phar = form.cleaned_data['pharmacy_id']
            pas = form.cleaned_data['password']
            pharm = Pharmacy.objects.filter(pharmacy_id=phar, password=pas)
            request.session['name'] = phar
            if pharm:
                return HttpResponseRedirect('/homepage')
            else:
                messages.error(request,'Invalid username or password')
    return render(request, 'Register_and_login/pharmacyLogin.html', context={'form': form})

def pharmacy_contact(request):
    form = PharmacyContact(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            number = form.cleaned_data['contact_no']
            alternate = form.cleaned_data['alternate_no']

            pharm = Pharmacy.objects.get(pharmacy_id = request.session['pharmacy'])

            inst = contact_pharmacy()
            first_contact = contact_pharmacy.objects.filter(pharmacy_id=pharm).first()
            if not first_contact:
                inst.default = "True"
            inst.pharmacy=pharm
            inst.contact_no=number
            inst.save()

            inst1 = contact_pharmacy()
            inst1.pharmacy = pharm
            inst1.contact_no = alternate
            inst1.save()
            return HttpResponseRedirect('/pharmacy/login')

    return render(request, 'Register_and_login/pharmacyContact.html', context={'form': form})


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

            user = customer.objects.get(username = request.session['user'])
            #user1=customer.objects.get(username=request.session['name'])
            print(user.username)
            #print(user1.username)

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

            return HttpResponseRedirect('/user/login')

    return render(request, 'Register_and_login/userContact.html', context={'form': form})
