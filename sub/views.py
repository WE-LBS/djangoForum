from django.shortcuts import render

from sub.models import Category
def category(request,category_from_url):
    context = {
        "category" : Category.objects.get(name=category_from_url),
    }
    return render(request,"sub/category.html",context)