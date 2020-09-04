
from django.urls import path
from . import views

#app_name = "main"

urlpatterns = [
	path("", views.index, name='index'),
	path("blog/<slug:slug>/", views.BlogDetailView, name="blog_detail"),
	path('allblogs/', views.AllBlogsView, name='all_blogs'),
	path('about/', views.about, name='about'),
	path('postblog/', views.PostBlogView, name='post_blog'),
]
