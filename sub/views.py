from django.shortcuts import render
from sub.forms import CreatePost

from sub.models import Category, Post, Comment, Name
def category(request,category_from_url):
    if request.method == "POST":
        form = CreatePost(request.POST)
        if form.is_valid():
            title = form.cleaned_data["title"]
            description = form.cleaned_data["description"]
            
            author = form.cleaned_data["author"]
            if Name.objects.filter(name=author).exists() == False:
                n = Name(name=author)
                n.save()
            author = Name.objects.get(name=author)

            category = Category.objects.get(name=category_from_url)
            p = Post(title=title,description=description,author=author,category=category)
            p.save()
            print("saved post")
            



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

def createPost(request,category_from_url):
    form = CreatePost
    context = {
        "form" : form,
        "category" : category_from_url,
    }
    return render(request,"sub/createPost.html",context)
