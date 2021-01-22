from django.shortcuts import render
from django.http import HttpResponse
from math import ceil
from .models import Product
# Create your views here.
def index(request):
    products= Product.objects.all()
    allProds=[]
    catprods= Product.objects.values('category', 'id')
    cats= {item["category"] for item in catprods}
    for cat in cats:
        prod=Product.objects.filter(category=cat)
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allProds.append([prod, range(1, nSlides), nSlides])

    params={'allProds':allProds }
    return render(request,"shop/index.html", params)

def about(request):
    return render(request,'shop/about.html');
def contact(request):
    return HttpResponse("shop contact page");
def tracker(request):
    return HttpResponse("shop tracker page");
def search(request):
    return HttpResponse("shop search page");
def productView(request):
    return HttpResponse("shop productView page");
def checkout(request):
    return HttpResponse("shop checkout page");