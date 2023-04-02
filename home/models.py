from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from ckeditor_uploader.fields import RichTextUploadingField


class Category(models.Model):
    creator = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    Thumbnail = models.ImageField(upload_to="Cat_thumbnails", blank=True, null=True)
    description = models.TextField(blank=True,null=True)
    created_date = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return str(self.id) + ': ' +self.name
    
class Sub_category(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
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
    # liked = models.ManyToManyField(User,default=None,blank=True,related_name='liked')
    Thumbnail = models.ImageField(upload_to="Thumbnails", blank=True, null=True)
    upload_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return str(self.id) + '-> ' +self.title

    def get_absolute_url(self):
        return reverse('home')
    # @property
    # def num_likes(self):
    #     return self.liked.all().count()
    
class Comment(models.Model):
    comment = models.TextField()
    blog_id = models.ForeignKey(Blog,on_delete=models.CASCADE)
    comment_date = models.DateTimeField(auto_now_add=True)
    def __str__ (self):
        return str(self.id) + ': '+ self.comment

# LIKE_CHOICES = (
#     ('Like','Like'),
#     ('Unlike','Unlike'),
# )
# # Create your models here.
# class Like(models.Model):
#     user= models.ForeignKey(User, on_delete=models.CASCADE)
#     post = models.ForeignKey(Blog, on_delete=models.CASCADE)
#     value = models.CharField(choices=LIKE_CHOICES,default='like',max_length=10)

#     def __str__(self):
#         return str(self.post)