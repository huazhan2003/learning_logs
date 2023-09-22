from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

app_name = 'users'
urlpatterns = [
    # 登录界面
    path('login/',auth_views.LoginView.as_view(),name='login'),
    # 注销界面
    path('logout/',auth_views.LogoutView.as_view(), name='logout'),
    # 注册界面
    path('register/', views.register, name='register'),
]