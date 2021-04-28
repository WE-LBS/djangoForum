from django.shortcuts import render

from sub.models import Category, Post, Comment
def category(request,category_from_url):
    if Category.objects.filter(name=category_from_url).exists() == False:
        context = {
            "missingCategory" : category_from_url,
        }
        return render(request,"sub/createCategory.html",context)

    category = Category.objects.get(name=category_from_url)

    
    
    
    posts = Post.objects.order_by("-pub_date").filter(category=category)
    context = {
        "category" : category,
        "posts" : posts,
    }
    return render(request,"sub/category.html",context)


def comments(request,category_from_url,post_id_from_url):

    context = {
        "post" : Post.objects.get(pk=post_id_from_url),
        "comments" : Comment.objects.filter(parent=Post.objects.get(pk=post_id_from_url))
    }
    return render(request,"sub/comments.html",context)

