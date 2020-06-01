from django.db import models

# Create your models here.

class About(models.Model):
    author = models.CharField(max_length=30)
    description = models.TextField()
    image = models.ImageField(upload_to="img/", blank=True, null=True, default='project3.png')

    def __str__(self): 
        return self.author 