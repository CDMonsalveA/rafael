from django.shortcuts import render

from home.models import Post, Comment

# Create your views here.
def index(request):
    return render(request, 'base.html')

def home(request):
    return render(request, 'base.html')

def services(request):
    return render(request, 'base.html')

def team(request):
    return render(request, 'base.html')

def contact(request):
    return render(request, 'base.html')

def blog_index(request):
    posts = Post.objects.all().order_by("-created_on")
    context = {
        "posts":posts,
    }
    return render(request, "blog/blog_index.html", context)

def blog_category(request, category):
    posts = Post.objects.filter(
        categories__name__contains=category
    ).order_by("-created_on")
    context = {
        "category": category,
        "posts": posts,
    }
    return render(request, "blog/category.html", context)

def blog_detail(request, pk):
    post = Post.objects.get(pk=pk)
    comments = Comment.objects.filter(post=post)
    context = {
        "post": post,
        "comments": comments,
    }

    return render(request, "blog/blog_detail.html", context)