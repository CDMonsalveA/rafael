from django.shortcuts import render

from home.models import Post, Comment

# Nav models
from home.models import NavBar, NavBarToggle

# Create your views here.
def index(request):
    # Get the navbar buttons
    navbar = NavBar.objects.all().order_by("order")
    # Get the navbar toggles
    navbartoggles = NavBarToggle.objects.all().order_by("order")
    context = {
        "navbar": navbar,
        "navbartoggles": navbartoggles,
    }
    return render(request, "base.html", context)

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