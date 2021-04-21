from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)
    

class Post(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=400)


class Comment(models.Model):
    description = models.CharField(max_length=200)