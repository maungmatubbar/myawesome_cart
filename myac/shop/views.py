from django.http import HttpResponse
from django.shortcuts import render
from django.db.models import QuerySet
from .models import Product
from math import ceil

# Create your views here.

def chunk_queryset(queryset: QuerySet, chunk_size: int):
    for i in range(0, len(queryset), chunk_size):
        yield queryset[i:i + chunk_size]

def index(request):
    products = Product.objects.all()
    n = len(products)
    nSlides = n//4 + ceil((n/4) - (n//4))
    # params = {
    #     'no_of_slides':nSlides,
    #     'range': range(1,nSlides),
    #     'product': products
    # }

    allProducts = [[products,range(1,nSlides), nSlides, {"product_title": "Mans Fashion"}],
                   [products,range(1,nSlides), nSlides, {"product_title": "Woman's Fashion"}]]
    params = {'allProds': allProducts}
    return render(request, 'shop/index.html', params)

def about(request):
    return render(request, 'shop/about.html')
def contact(request):
    return HttpResponse('This is contact page')
def tracker(request):
    return HttpResponse('This is tracker page')
def product_view(request):
    return HttpResponse('This is product view page')
def checkout(request):
    return HttpResponse('This is checkout page')
def cart(request):
    return HttpResponse('This is cart page')