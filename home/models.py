from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from ckeditor_uploader.fields import RichTextUploadingField


class Category(models.Model):
    creator = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    created_date = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return str(self.id) + ': ' +self.name
    
class Sub_category(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    created_by = models.ForeignKey(User,on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.category.name + '-> '+ self.name

class Blog(models.Model):
    author = models.ForeignKey(User,on_delete= models.CASCADE)
    slug = models.SlugField(unique=True,null=False,blank=False)
    title = models.CharField(max_length=200,blank=False,null=False)
    category = models.ForeignKey(Sub_category,on_delete=models.CASCADE)
    content = RichTextUploadingField()
    upload_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return str(self.id) + '-> ' +self.title
    
class Comment(models.Model):
    comment = models.TextField()
    blog_id = models.ForeignKey(Blog,on_delete=models.CASCADE)
    comment_date = models.DateTimeField(auto_now_add=True)
    def __str__ (self):
        return str(self.id) + ': '+ self.comment

# Create your models here.
