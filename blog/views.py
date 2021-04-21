from django.shortcuts import render,HttpResponse,Http404
from django.views import generic
from . models import Blog
from django.template import loader

# Create your views here.
def index(request):
    blogs=Blog.objects.all()
    template=loader.get_template("blog/index.html")
    context={
        'blogs':blogs,
    }
    return HttpResponse(template.render(context,request))

def details(request,blog_id):

    try:
        blog=Blog.objects.get(pk=blog_id)

    except Blog.DoesNotExist:
        raise Http404("something is wrong")
    return render(request,"blog/detail.html",{'blog':blog})
