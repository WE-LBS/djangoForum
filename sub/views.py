from django.shortcuts import render

from sub.models import Category, Post
def category(request,category_from_url):
    category = Category.objects.get(name=category_from_url)
    posts = Post.objects.order_by("-pub_date").filter(category=category)
    context = {
        "category" : category,
        "posts" : posts,
    }
    return render(request,"sub/category.html",context)