from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello world, You are at blog's index")

def detail(request,post_id):
    return HttpResponse("You are viewing post detail page. And ID is ")