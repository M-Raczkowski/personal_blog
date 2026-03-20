from django.shortcuts import render, redirect
from blog.models import Post, Comment, Photo, Author
from django.http import HttpResponseRedirect
from blog.forms import CommentForm, PhotoForm

def blog_index(request):
    all_posts = Post.objects.all().order_by("-created_on")

    hero_posts = all_posts[:3]
    posts = all_posts[3:11]

    return render(request, "blog/index.html", {
        "posts": posts,
        "hero_posts": hero_posts
    })

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
    author = Author.objects.get(pk=pk)
    form = CommentForm()
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(
                author=form.cleaned_data["author"],
                body=form.cleaned_data["body"],
                post=post
            )
            comment.save()
            return HttpResponseRedirect(request.path_info)
    comments = Comment.objects.filter(post=post)
    context = {
        "post" : post,
        "comments" : comments,
        "form" : form,
        "author" : author,
    }
    return render(request, "blog/detail.html", context)



def blog_categories(request):
    return render(request, "blog/categories.html")
def blog_about(request):
    return render(request, "blog/about.html")

def blog_contact(request):
    return render(request, "blog/contact.html")

