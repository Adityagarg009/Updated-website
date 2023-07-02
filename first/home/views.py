from django.shortcuts import render,HttpResponse
from home.models import Sign
from datetime import datetime
# Create your views here.
def index(request):
    context={
        'variable':"this is sent"
    }
    #return HttpResponse("this homepage")
    return render(request, 'wow.html',context)
def about(request):
    #return HttpResponse("this is about page")

    return render(request,'about.html')
def contact(request):
    #return HttpResponse("this is contact page")
    return render(request,'contact.html')
def order(request):
    #return HttpResponse("this order page")
    return render(request,'order.html')
def wishlist(request):
    #return HttpResponse("this wishlist page")
    return render(request,'wishlist.html')
def coupons(request):
    #return HttpResponse("this coupon page")
    return render(request,'coupons.html')
def home(request):
    return render(request,'wow.html')
def sign(request):
    if request.method=='POST':
        name =request.POST.get('name')
        email =request.POST.get('email')
        password =request.POST.get('password')
        address =request.POST.get('address')
        address2 =request.POST.get('address2')
        city =request.POST.get('city')
        state =request.POST.get('state')
        phone =request.POST.get('phone')
        sign=Sign(name=name,email=email,password=password,address=address,address2=address2,city=city,state=state,phone=phone,date=datetime.today() )
    return render(request,'sign.html')