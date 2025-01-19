from django.http import HttpResponse
from django.shortcuts import render
from .models import Blog
# Create your views here.
def index(request):
    
    return render(request, 'blog/index.html')

def blogpost(request, id):
    post = Blog.objects.filter(post_id = id)[0]
    print(post)


    return render(request, 'blog/blogpost.html',{'post':post})