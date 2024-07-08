from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.urls import reverse #url name ah vachchu redirect panna use aakum
import logging
from .models import Post
from django.http import Ht

# Create your views here.
# static demo data
# posts=[
#         {'id':1,'title':'Post 1','content':'Content of Post 1'},
#         {'id':2,'title':'Post 2','content':'Content of Post 2'},
#         {'id':3,'title':'Post 3','content':'Content of Post 3'},
#         {'id':4,'title':'Post 4','content':'Content of Post 4'},

#     ]
def index(request):
    blog_title="Latest Posts"
    
    #getting data from post model 
    posts=Post.objects.all()
    return render(request,'blog/index.html',{'blog_title':blog_title,'posts':posts})#variable interpolation

def detail(request,post_id):
    # static data
    # post=next((item for item in posts if item['id']==int(post_id)),None)

    try:
        # getting data from model by post id
        post=Post.objects.get(pk=post_id)#pk is the primary key
    
    except Post.DoesNotExist:
        raise Http404("Post Does not Exist!")

    # logger=logging.getLogger("TESTING")
    # logger.debug(f'post variable is {post}')#it will show the string in terminal
    return render(request,'blog/detail.html',{'post':post})

def old_url_redirect(request):
    return redirect(reverse('blog:new_page_url'))

def new_url_view(request):
    return HttpResponse("This is the new URL")