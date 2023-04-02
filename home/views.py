from django.core.paginator import Paginator
from django.shortcuts import render,HttpResponse,redirect,HttpResponseRedirect
from .models import *
from .forms import *
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.contrib import messages
from django.views.generic import TemplateView,UpdateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import FormView
from django.contrib.auth  import authenticate,  login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin

def deleteComment(request):
        comment_id = request.POST['comment']
        comment = Comment.objects.get(id = comment_id)
        comment.delete()
        referer = request.META.get('HTTP_REFERER')
        return HttpResponseRedirect(referer)

def commentSave(request):
    if request.method == "POST":
        slug = request.POST['slug']
        content = request.POST['content']
        comment = Comment(blog_id=Blog.objects.get(slug=slug), comment=content)
        comment.save()
        referer = request.META.get('HTTP_REFERER')
        return HttpResponseRedirect(referer)


@login_required(login_url = '/login')
def Delete_Blog_Post(request, slug):
    data= User.objects.get(id=request.user.id)
    posts = Blog.objects.get(slug=slug)
    if request.method == "POST":
        posts.delete()
        return redirect('/')
    return render(request, 'delete_blog_post.html', {'posts':posts,'data':data})


class UpdatePostView(LoginRequiredMixin,UpdateView):
    model = Blog
    template_name = 'register.html'
    fields = '__all__'
    success_url = reverse_lazy('home')


def Category_search(request):
    page_id = request.GET['Page']
    Sub_cat = Sub_category.objects.filter(category = page_id).order_by('name')
    cat = Category.objects.filter(id= page_id)
    desc = ''
    for i in cat:
        desc = i.description

    context = {
        'subcat': Sub_cat,
        'desc' : desc,
        'page_id': page_id,
        'posts': '',
    }

    if request.method == 'GET':
        searched = request.GET['Category']
        posts = Blog.objects.filter(category__name = searched,category__category= page_id).order_by('-upload_date')
        paginator = Paginator(posts, 7) # Show 25 contacts per page.
        page_number = request.GET.get('page')
        posts = paginator.get_page(page_number)
        context['posts'] =  posts
        context['searched'] = searched
        
        return render(request, "Category.html", context)
    else:
        context['searched'] = 'null'
        return render(request, "Category.html", context)


def search(request):
    page_id = request.POST['page']
    if page_id == '' :
        cat = Category.objects.all()
        Sub_cat = Sub_category.objects.all()
    else:  
        Sub_cat = Sub_category.objects.filter(category = page_id).order_by('name')
        cat = Category.objects.filter(id= page_id)
    desc = ''
    for i in cat:
        desc = i.description

    context = {
        'subcat': Sub_cat,
        'desc' : desc,
        'page_id': page_id,
        'posts': ''
    }

    if request.method == 'POST':
        searched = request.POST['searched']
        if page_id == '' :
            posts = Blog.objects.filter(title__contains=searched).order_by('-upload_date')
        else:
            posts = Blog.objects.filter(title__contains=searched,category__category= page_id).order_by('-upload_date')
        paginator = Paginator(posts, 7) # Show 25 contacts per page.
        page_number = request.GET.get('page')
        posts = paginator.get_page(page_number)
        context['posts'] =  posts
        context['searched'] = searched
        return render(request, "Category.html", context)
    else:
        context['searched'] = 'null'
        return render(request, "Category.html", context)


def sub_cats(request,id):
        Sub_cat = Sub_category.objects.filter(category = id).order_by('name')
        cat = Category.objects.filter(id= id)
        posts = Blog.objects.filter(category__category= id).order_by('-upload_date')
        paginator = Paginator(posts, 7) # Show 25 contacts per page.
        page_number = request.GET.get('page')
        posts = paginator.get_page(page_number)
        desc = ''
        for i in cat:
            desc = i.description
        context = {
            'subcat': Sub_cat,
            'desc' : desc,
            'posts': posts,
            'page_id': int(id),
        }
        context['searched'] = 'null'
        return render(request,'Category.html',context)



class UserLoginView(LoginView):
    redirect_authenticated_user = True
    template_name = 'Login.html'
    
    def get_success_url(self):
        return reverse_lazy('home') 
    
    def form_invalid(self, form):
        messages.error(self.request,'Invalid username or password')
        return self.render_to_response(self.get_context_data(form=form))


class BlogDetailView(DetailView):

    model = Blog

    def get(self, request, *args, **kwargs):
        data = Blog.objects.get(slug=kwargs['slug'])
        posts = Comment.objects.filter(blog_id__slug = kwargs['slug']).order_by('-comment_date')
        counts = Comment.objects.filter(blog_id__slug = kwargs['slug']).count()
        paginator = Paginator(posts, 7) # Show 25 contacts per page.
        page_number = request.GET.get('page')
        posts = paginator.get_page(page_number)
        context = {'data': data,'posts':posts,'counts':counts}
        return render(request, 'DetailedBlog.html',context)

    def get_context_data(self,request,*args,**kwargs):
        data = Blog.objects.get(slug=kwargs['slug'])
        posts = Comment.objects.filter(blog_id__slug = kwargs['slug']).order_by('-comment_date')
        counts = Comment.objects.filter(blog_id__slug = kwargs['slug']).count()
        paginator = Paginator(posts, 7) # Show 25 contacts per page.
        page_number = request.GET.get('page')
        posts = paginator.get_page(page_number)
        context = {'data': data,'posts':posts,'counts':counts}
        context = {'data': data}
        return context

def home(request):
    data = Blog.objects.all().order_by('-upload_date')
    cat = Category.objects.all()
    context = {
        'data':data,
        'cat':cat
    }
    return render(request,'home.html',context)



class Blogview(LoginRequiredMixin,FormView):
    initial = {
    }
    
    template_name = 'register.html'
    form_class = blogForm
    success_url = '/'
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_heading'] = 'Register a Blog'
        context['title'] = 'Add Blog'
        return context

    def form_valid(self, form):

        Author = form.cleaned_data['author']
        Slug = form.cleaned_data['slug']
        Title = form.cleaned_data['title']
        Category = form.cleaned_data['category']
        Content = form.cleaned_data['content']
        Thumbnails = form.cleaned_data['Thumbnail']
        obj = Blog(author = Author,slug = Slug, title = Title, category = Category,content = Content,Thumbnail = Thumbnails)
        obj.save()

        return super().form_valid(form)


class Categoryview(LoginRequiredMixin,FormView):
    initial = {
    }
    
    template_name = 'register.html'
    form_class = categoryForm
    success_url = '/'
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_heading'] = 'Register a Category'
        context['title'] = 'Add Category'
        return context

    def form_valid(self, form):
        form.save(commit=True)
        return super().form_valid(form)

class SubCategoryview(LoginRequiredMixin,FormView):
    initial = {
    
    }
    
    template_name = 'register.html'
    form_class = sub_categoryForm
    success_url = '/'
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_heading'] = 'Register a SubCategory'
        context['title'] = 'Add SubCategory'
        return context

    def form_valid(self, form):
        form.save(commit=True)
        return super().form_valid(form)

class userCreateview(LoginRequiredMixin,FormView):
    initial = {
    
    }
    
    template_name = 'register.html'
    form_class = userForm
    success_url = '/'
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_heading'] = 'Register a User'
        context['title'] = 'Add User'
        return context

    def form_valid(self, form):
        form.save(commit=True)
        return super().form_valid(form)


@login_required
def Logout(request):
    logout(request)
    return redirect('home')
