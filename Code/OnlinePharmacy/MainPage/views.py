from django.http import HttpResponse
from django.shortcuts import render
from cart.models import contains
from Register_and_login import forms
from customer.models import customer
from pharmacy.models import Pharmacy
from customer.forms import customerForm

def homepage(request):
    print (request.session['name'])
    try :
        user = customer.objects.get(username=request.session['name'])
        print(user.cart_id)

        cart = contains.objects.filter(cart_id_id=user)
        count = 0
        for cart_id in cart:
            print(cart_id)
            count = count + 1
        print(count)
        return render(request,'customer/homepage.html',{'user': user,'items_in_cart':count})
        #return render(request, 'customer/homepage.html', {'user': user})
    except:
        try:
            print ('helo')
            user=Pharmacy.objects.get(pharmacy_id=request.session['name'])
            return render(request,'pharmacy/dashboard.html',{'pharmacy':user })
        except:
            return HttpResponse('<h1>sorry </h1>')


def userPage(request):
    return render(request,'MainPage/mainpage.html')