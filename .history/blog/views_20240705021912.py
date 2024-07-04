from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.urls import reverse #url name ah vachchu redirect panna use aakum

# Create your views here.
def index(request):
    return render(request,'blogindex.html')

def detail(request,post_id):
    return HttpResponse(f"You are viewing post detail page. And ID is {post_id}")

def old_url_redirect(request):
    return redirect(reverse('blog:new_page_url'))

def new_url_view(request):
    return HttpResponse("This is the new URL")