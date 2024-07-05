from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.urls import reverse #url name ah vachchu redirect panna use aakum

# Create your views here.
def index(request):
    blog_title="Latest osts"
    return render(request,'blog/index.html',{'blog_title':blog_title})

def detail(request,post_id):
    return render(request,'blog/detail.html')

def old_url_redirect(request):
    return redirect(reverse('blog:new_page_url'))

def new_url_view(request):
    return HttpResponse("This is the new URL")