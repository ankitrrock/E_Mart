from django.shortcuts import render
from django.http import HttpResponse
from .models import registration



# Create your views here.


def about(request):
    return render(request, "about.html")

def checkout(request):
    return render(request, "checkout.html")

def dresses(request):
    return render(request, "dresses.html")
def faq(request):
    return render(request, "faq.html")

def jeans(request):
    return render(request, "jeans.html")
def mail(request):
    return render(request, "mail.html")

def products(request):
    return render(request, "products.html")

def salwars(request):
    return render(request, "salwars.html")

def sandals(request):
    return render(request, "sandals.html")

def sarees(request):
    return render(request, "sarees.html")

def shirts(request):
    return render(request, "shirts.html")


def single(request):
    return render(request, "single.html")

def skirts(request):
    return render(request, "skirts.html")
    
def sweaters(request):
    return render(request, "sweaters.html") 

def index(request):
    return render(request, "index.html")  

def short_codes(request):
    return render(request, "short_codes.html") 

def register(request):
    webdata = registration()
    webdata.u_name = request.POST.get('u_name')
    webdata.u_email = request.POST.get('u_email')
    webdata.u_password = request.POST.get('u_password')
    webdata.u_cpassword = request.POST.get('u_cpassword')
    webdata.save()    
    return render(request,'about.html')    








