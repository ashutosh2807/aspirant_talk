from django.shortcuts import render,HttpResponse
from .models import *
# Create your views here.
def home(request):
    data = Blog.objects.all()
    context = {
        'data':data
    }
    return render(request,'home.html',context)