from django.shortcuts import render,redirect
from .models import restaurants,customers
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

def details(request,u_id):
    user=customers.objects.get(pk=u_id)
    return render(request,'details.html',{'u':user})

def register(request):
    if request.method=='POST':
        user_name = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        cust_name = request.POST['name']
        cust_ph = request.POST['ph']
        cust_mail = request.POST['mail']
        cust_gen = request.POST['gender']
        cust_dnum = request.POST['dnum']
        cust_snum = request.POST['snum']
        cust_loc = request.POST['loc']
        cust_city = request.POST['city']
        cust_pin = request.POST['pin']
        if password1==password2:
            if User.objects.filter(username=user_name).exists():
                messages.info(request,'Username Taken')
                return redirect('register')
            else:
                user = User.objects.create_user(username=user_name,password=password1)
                user.save()
                cust = customers.objects.create(CUST_NAME=cust_name,CUST_PH=cust_ph,CUST_MAIL=cust_mail,CUST_GEN=cust_gen,CUST_DNUM=cust_dnum,CUST_SNUM=cust_snum,CUST_LOC=cust_loc,CUST_CITY=cust_city,CUST_PIN=cust_pin)
                isinstance.cust
                cust.save()
                return redirect('details', user.id)
        else:
            messages.info(request,'Passwords not Matching')
            return render(request,'register.html')

    else:
        return render(request, 'register.html')