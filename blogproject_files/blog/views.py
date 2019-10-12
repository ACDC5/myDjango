from django.shortcuts import render
from django.http.response import HttpResponse
from blog.models import Post
from datetime import datetime
from django.http import Http404

# Create your views here.
def myPage(request):
    return HttpResponse("<h1>向用户展示的页面</h1>")

def detail(request, my_args):
    return HttpResponse("You're looking at my_args= %s" % my_args)

def sqlQuery(request):
    post = Post.objects.all()
    # ids = Post.objects.get(category_id=1)
   # 1 B = []
   #  for a in range(post):
   #      B = B.append(a)

    # str = ("title = %s,category_id = %s,excerpt = %s"
    #       % (post.title,post.category_id,post.excerpt))
    return HttpResponse(post)

'''经过试图调用模板(模板中的内容一般为静态的html、css、js网页)
template和view一般被当作MVC中的V层，view用于请求的逻辑处理，template展示经view处理过的数据页面'''
def myTemplate(request):
    return render(request,'test.html',{'current_time':datetime.now(),'value_Kye':'若批评不自由，则赞美无意义'})

def home(request):
    post_list = Post.objects.all() #获取所有Post对象
    return render(request,'home.html',{'post_list':post_list})

def demo(request, id):
    try:
        post = Post.objects.get(id=str(id))
    except Post.DoesNotExist:
        raise Http404
    return render(request,'post.html',{'post':post})