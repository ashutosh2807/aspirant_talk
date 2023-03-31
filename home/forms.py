from django import forms
from django.contrib.auth.models import User
from .models import *
from ckeditor_uploader.widgets import CKEditorUploadingWidget
# class 

class blogForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())
    class Meta:
        model = Blog
        fields = "__all__"


class sub_categoryForm(forms.ModelForm):
    class Meta:
        model = Sub_category
        fields = "__all__"


class categoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = "__all__"

class userForm(forms.ModelForm):
    class Meta:
        model = User
        fields = "__all__"