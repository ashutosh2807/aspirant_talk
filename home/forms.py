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