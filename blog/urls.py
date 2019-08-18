from django.urls import path
from .import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('',views.allblogs,name='blogsname'),
    path('<int:blog_id>/',views.detail,name="detailname"),
    path('login/', views.user_login, name='login'),
    path('signup/', views.register, name='signup'),
    path('/', views.user_logout, name='logout'),


]
