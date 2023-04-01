from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView
from aspirant_talk import settings


urlpatterns = [
    path('', views.home,name='home'),
    path('addBlog/',views.Blogview.as_view()),
    path('addCategory/',views.Categoryview.as_view()),
    path('addSubCategory/',views.SubCategoryview.as_view()),
    path('addAuser/',views.userCreateview.as_view()),
    path('blog/<slug:slug>/', views.BlogDetailView.as_view()),
    path("Category/<int:id>", views.sub_cats, name="subcat_search"),
    path('login/', views.UserLoginView.as_view(),name='login'),
     path('logout/', LogoutView.as_view(next_page='home'),name='logout')

    # path('logout/', LogoutView.as_view(next_page=settings.LOGOUT_REDIRECT_URL), name='logout'),
]
