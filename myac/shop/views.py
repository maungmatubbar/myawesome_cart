from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'shop/index.html')

def about(request):
    return HttpResponse('This is about page')
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