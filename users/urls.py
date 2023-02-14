from django.urls import path
from . import views


urlpatterns = [
    path('login', views.loginUser, name='login'),
    path('logout', views.logoutUser, name='logout'),
    path('register', views.registerUser, name='register'),

    path('', views.profiles, name='profiles'),
    path('user_profile/<str:pk>/', views.userProfile, name='user_profile'),
]