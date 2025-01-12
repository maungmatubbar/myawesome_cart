from django.http import HttpResponse
from django.shortcuts import render
from django.db.models import QuerySet
from django.template.context_processors import request

from .models import Product, Contact, Orders, OrderUpdate
from math import ceil
import json
# Create your views here.

def chunk_queryset(queryset: QuerySet, chunk_size: int):
    for i in range(0, len(queryset), chunk_size):
        yield queryset[i:i + chunk_size]

def index(request):
    allProducts = []
    catProds = Product.objects.values('category','id')
    cats = {item['category'] for item in catProds}
    for cat in cats:
        prod = Product.objects.filter(category = cat)
        n = len(prod)
        nSlides = n//4 + ceil((n/4) - (n//4))
        allProducts.append([prod, range(1, nSlides),nSlides])
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
    if request.method == "POST":
        orderId = request.POST.get('orderId', '')
        email = request.POST.get('email', '')
        try: 
            order = Orders.objects.filter(order_id=orderId,email=email)
            if len(order)>0:
                update = OrderUpdate.objects.filter(order_id=orderId)
                updates = []
                for item in update:
                    updates.append({'text': item.update_desc, 'time': item.timestamp})
                    response = json.dumps(updates, default=str)
                return HttpResponse(response)
            else:
                return HttpResponse('{}')
        except Exception as e:
            return HttpResponse('{}')
    return render(request, 'shop/tracker.html')
def product_view(request,id):
    #Fetch the product using the id
    product = Product.objects.filter(id=id)

    return render(request, 'shop/product_view.html',{
        'product': product[0]
    })
def checkout(request):
    if request.method == 'POST':
        items_json = request.POST.get('itemsJson','')
        name = request.POST.get('name', '')
        email = request.POST.get('email','')
        address = request.POST.get('address','')
        phone = request.POST.get('phone','')
        city = request.POST.get('city','')
        state = request.POST.get('state','')
        zip_code = request.POST.get('zip_code','')
        order = Orders(items_json=items_json, name=name, email=email, phone=phone, address=address, city=city, state=state, zip_code=zip_code)
        order.save()
        orderUpdate = OrderUpdate(order_id=order.order_id, update_desc="The order has been placed")
        orderUpdate.save()
        thank = True
        return render(request, 'shop/checkout.html', {'thank':thank, 'id':order.order_id})
    return render(request, 'shop/checkout.html')
def cart(request):
    return render(request, 'shop/cart.html')
def search(request):
    return render(request, 'shop/search.html')