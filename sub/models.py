from django.db import models
from django.utils import timezone



# Create your models here.

class Name(models.Model):
    name = models.CharField(max_length=100)
    joined = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=200,null=False)
    description = models.CharField(max_length=400)
    author = models.ForeignKey(Name,on_delete=models.CASCADE,null=True)

    pub_date = models.DateTimeField(default=timezone.now)
    category = models.ForeignKey(Category,on_delete=models.CASCADE,null=True)
    def __str__(self):
        return self.title


class Comment(models.Model):
    parent = models.ForeignKey(Post,on_delete=models.CASCADE,null=True)
    description = models.CharField(max_length=200)
    author = models.ForeignKey(Name,on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.description


