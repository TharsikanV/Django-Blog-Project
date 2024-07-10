from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.urls import reverse #url name ah vachchu redirect panna use aakum
import logging
from .models import Post
from django.http import Http404
from django.core.paginator import Paginator
from .forms import ContactForm

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
    all_posts=Post.objects.all()

    # paginate
    paginator=Paginator(all_posts,5)#kidaikkira object ah ipd vankidan
    page_number=request.GET.get('page')
    page_obj=paginator.get_page(page_number)

    return render(request,'blog/index.html',{'blog_title':blog_title,'page_obj':page_obj})#variable interpolation

def detail(request,slug):
    # static data
    # post=next((item for item in posts if item['id']==int(post_id)),None)

    try:
        # getting data from model by post id
        # post=Post.objects.get(pk=post_id)#pk is the primary key
        post=Post.objects.get(slug=slug)
        related_posts=Post.objects.filter(category=post.category).exclude(pk=post.id)

    except Post.DoesNotExist:
        raise Http404("Post Does not Exist!")

    # logger=logging.getLogger("TESTING")
    # logger.debug(f'post variable is {post}')#it will show the string in terminal
    return render(request,'blog/detail.html',{'post':post,'related_posts':related_posts})

def old_url_redirect(request):
    return redirect(reverse('blog:new_page_url'))

def new_url_view(request):
    return HttpResponse("This is the new URL")

def contact_view(request):
    if request.method == 'POST':
        form=ContactForm(request.POST)

        name=request.POST.get('name')
        email=request.POST.get('email')
        message=request.POST.get('message')

        logger=logging.getLogger("TESTING")
        if form.is_valid():
            logger.debug(f'post Data is {form.cleaned_data['name']} {form.cleaned_data['email']} {form.cleaned_data['message']}')#it will show the string in terminal
            # send email or svae in database
            success_message='Your Email has been sent!'
            return render(request,'blog/contact.html',{'form':form,'success_message':success_message})
        else:
            logger.debug('Form validation failure')
        return render(request,'blog/contact.html',{'form':form,'name':name,'email':email,'message':message})
    return render(request,'blog/contact.html')