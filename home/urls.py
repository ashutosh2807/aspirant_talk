from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView
from aspirant_talk import settings

app_name= 'home'

urlpatterns = [
    path('', views.home),
    path('addBlog/',views.Blogview.as_view()),
    path('addCategory/',views.Categoryview.as_view()),
    path('addSubCategory/',views.SubCategoryview.as_view()),
    path('addAuser/',views.userCreateview.as_view()),
    path('blog/<slug:slug>/', views.BlogDetailView.as_view()),

    # path('logout/', LogoutView.as_view(next_page=settings.LOGOUT_REDIRECT_URL), name='logout'),
]
