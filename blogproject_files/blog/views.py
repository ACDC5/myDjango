from django.shortcuts import render
from django.http.response import HttpResponse

# Create your views here.
def myPage(request):
    return HttpResponse("<h1>向用户展示的页面</h1>")

def detail(request, my_args):
    return HttpResponse("You're looking at my_args %s=" % my_args)