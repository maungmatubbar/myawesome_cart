from django.http import HttpResponse
from django.shortcuts import render
from django.db.models import QuerySet
from .models import Product, Contact
from math import ceil

# Create your views here.

def chunk_queryset(queryset: QuerySet, chunk_size: int):
    for i in range(0, len(queryset), chunk_size):
        yield queryset[i:i + chunk_size]

def index(request):
    # products = Product.objects.all()
    # n = len(products)
    # nSlides = n//4 + ceil((n/4) - (n//4))
    # params = {
    #     'no_of_slides':nSlides,
    #     'range': range(1,nSlides),
    #     'product': products
    # }
    allProducts = []
    catProds = Product.objects.values('category','id')
    cats = {item['category'] for item in catProds}
    for cat in cats:
        prod = Product.objects.filter(category = cat)
        n = len(prod)
        nSlides = n//4 + ceil((n/4) - (n//4))
        allProducts.append([prod, range(1, nSlides),nSlides])
    # print(allProducts)
    # allProducts = [[products,range(1,nSlides), nSlides, {"product_title": "Mans Fashion"}],
    #                [products,range(1,nSlides), nSlides, {"product_title": "Woman's Fashion"}]]
    params = {'allProds': allProducts}
    return render(request, 'shop/index.html', params)

def about(request):
    return render(request, 'shop/about.html')
def contact(request):
    if request.method == "POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        desc = request.POST.get('desc', '')
        contact = Contact(name=name, email=email, phone=phone, desc=desc)
        contact.save()

    return render(request, 'shop/contact.html')
def tracker(request):
    return render(request, 'shop/tracker.html')
def product_view(request,id):
    #Fetch the product using the id
    product = Product.objects.filter(id=id)

    return render(request, 'shop/product_view.html',{
        'product': product[0]
    })
def checkout(request):
    return render(request, 'shop/about.html')
def cart(request):
    return render(request, 'shop/cart.html')
def search(request):
    return render(request, 'shop/search.html')