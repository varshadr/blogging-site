from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from froala_editor.fields import FroalaField

from home.helpers import generate_slug





class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_verified = models.BooleanField(default=False)
    token = models.CharField(max_length=100)


class BlogModel(models.Model):
    title = models.CharField(max_length=1000)
    content = FroalaField()#editor which we will integrate as it has many good features
    
    slug = models.SlugField(max_length=1000, null=True, blank=True)# 
    user = models.ForeignKey(User, blank=True, null=True,
                             on_delete=models.CASCADE)
    image = models.ImageField(upload_to='blog')#we will add these to static file
    created_at = models.DateTimeField(auto_now_add=True) #Create for one time
    upload_to = models.DateTimeField(auto_now=True)#this is to update


    def __str__(self):
        return self.title


    def save(self, *args, **kwargs):
        self.slug = generate_slug(self.title)
        super(BlogModel, self).save(*args, **kwargs)
