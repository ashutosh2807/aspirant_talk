from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('addBlog/',views.Blogview.as_view())
]
