from django.shortcuts import render
from blog.models import Post
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


def blog_index(request):
    all_posts = Post.objects.all().order_by("-created_on")
    hero_posts = all_posts[:3]
    posts = all_posts[3:]
    paginator = Paginator(posts, 4)
    page_number = request.GET.get('page',1)

    try:
        page_obj = paginator.page(page_number)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)

    return render(request, "blog/index.html", {
        "posts": posts,
        "hero_posts": hero_posts,
        "page_obj": page_obj
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
    context = {
        "post": post,
        "author": post.author,
    }
    template = "blog/single-standard.html"
    return render(request, template, context)



def blog_categories(request):
    return render(request, "blog/categories.html")
def blog_about(request):
    return render(request, "blog/about.html")

def blog_contact(request):
    return render(request, "blog/contact.html")

