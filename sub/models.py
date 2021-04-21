from django.db import models
from django.utils import timezone

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=400)
    pub_date = models.DateTimeField(default=timezone.now)
    category = models.ForeignKey(Category,on_delete=models.CASCADE,null=True)
    def __str__(self):
        return self.title


class Comment(models.Model):
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.description