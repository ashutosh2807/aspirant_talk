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
    path("search/", views.search, name="search"),
    path("edit_blog_post/<str:slug>/", views.UpdatePostView.as_view(), name="edit_blog_post"),
    path("delete_blog_post/<str:slug>/", views.Delete_Blog_Post, name="delete_blog_post"),
    path("Category_search/", views.Category_search, name="Category_search"),
    path('logout/', LogoutView.as_view(next_page='home'),name='logout'),
    path('deleteComment/',views.deleteComment, name="comment"),
    path('commentSave/',views.commentSave, name="comment")

    # path('logout/', LogoutView.as_view(next_page=settings.LOGOUT_REDIRECT_URL), name='logout'),
]
