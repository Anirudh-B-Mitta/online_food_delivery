from django.shortcuts import render,redirect
from .models import restaurants,customers,menu
from django.contrib.auth.models import User,auth
from django.contrib import messages

# Create your views here.

def index(request):
    return render(request, 'index.html')

def restaurents(request):
    res_list=restaurants.objects.all()
    return render(request, 'restaurents.html', {'res_list':res_list})

def about_us(request):
    return render(request, 'about_us.html')

def partner(request):
    return render(request,'partner.html')

def jobs(request):
    return render(request, 'job.html')

def stories(request):
    return render(request,'stories.html')

def details(request):
    if request.method=='POST':
        cust_name = request.POST['name']
        cust_ph = request.POST['ph']
        cust_mail = request.POST['mail']
        cust_gen = request.POST['gender']
        cust_dnum = request.POST['dnum']
        cust_snum = request.POST['snum']
        cust_loc = request.POST['loc']
        cust_city = request.POST['city']
        cust_pin = request.POST['pin']
        cust = customers.objects.create(CUST_ID_id=request.user.id,CUST_NAME=cust_name,CUST_PH=cust_ph,CUST_MAIL=cust_mail,CUST_GEN=cust_gen,CUST_DNUM=cust_dnum,CUST_SNUM=cust_snum,CUST_LOC=cust_loc,CUST_CITY=cust_city,CUST_PIN=cust_pin)
        cust.save()
        return redirect('index')
    else:
        return render(request,'details.html')

def register(request):
    if request.method=='POST':
        user_name = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1==password2:
            if User.objects.filter(username=user_name).exists():
                messages.info(request,'Username Taken')
                return redirect('register')
            else:
                user = User.objects.create_user(username=user_name,password=password1)
                user.save()
                return redirect('details')
        else:
            messages.info(request,'Passwords not Matching')
            return render(request,'register.html')

    else:
        return render(request, 'register.html')

def menu_(request,rid):
    menu_list=menu.objects.all()
    if request.method == 'POST':
        dish=request.POST['dish']
        cart=request.session.get('cart')
        if cart:
            if cart.get(dish):
                cart[dish]=cart.get(dish)+1
            else:
                cart[dish]=1
        else:
            cart={}
            cart[dish]=1
        print(cart)
        request.session['cart']=cart

    elif request.method == 'GET':
        request.session['cart']={}

    rest=restaurants.objects.get(pk=rid)
    return render(request,'menu.html',{'menu_list':menu_list,'rest':rest})

def billing(request,ord):
    total=0
    for cost in ord.values():
        total+=int(cost)
    return render(request,'billing.html',{'total':total,'ord':ord})