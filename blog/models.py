from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self): 
        return self.name 


class Post(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to="img/", blank=True, null=True)
    categories = models.ManyToManyField('Category', related_name='posts')

    def __str__(self): 
        return self.title 

class Comment(models.Model):
    author = models.CharField(max_length=64)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey('Post', on_delete=models.CASCADE)

    def __str__(self): 
        return self.author 

    
