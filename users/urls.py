from django.urls import path
from . import views


urlpatterns = [
    path('login', views.loginUser, name='login'),
    path('logout', views.logoutUser, name='logout'),
    path('register', views.registerUser, name='register'),
    path('account', views.userAccount, name='account'),
    path('edit_account', views.editAccount, name='edit_account'),
    path('add_skill', views.createSkill, name='add_skills'),

    path('', views.profiles, name='profiles'),
    path('user_profile/<str:pk>/', views.userProfile, name='user_profile'),
]