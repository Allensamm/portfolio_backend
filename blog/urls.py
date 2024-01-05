# blog/urls.py
from django.urls import path
from .views import PostList
from blog.views import CustomTokenObtainPairView
from . import views	
from django.contrib import admin


urlpatterns = [
    path('posts/', PostList.as_view(), name='post-list'),
    path('register/', views.UserRegister.as_view(), name='register/'),
    path('posts/', PostList.as_view(), name='post-list'),
    path('posts/<str:category>/', PostList.as_view(), name='post-list-filtered'),
	path('login/', views.UserLogin.as_view(), name='login'),
	path('logout/', views.UserLogout.as_view(), name='logout'),
	path('user/', views.UserView.as_view(), name='user'),
    path('token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair')
]

