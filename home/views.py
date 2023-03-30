from django.shortcuts import render,HttpResponse
from .models import *
from .forms import *
from django.views.generic import TemplateView
from django.views.generic.edit import FormView


def home(request):
    data = Blog.objects.all()
    context = {
        'data':data
    }
    return render(request,'home.html',context)


class Blogview(FormView):
    initial = {
    
    }
    
    template_name = 'register.html'
    form_class = blogForm
    success_url = '/'
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_heading'] = 'Register a Blog'
        return context

    def form_valid(self, form):
        form.save(commit=True)
        return super().form_valid(form)
