from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
urlpatterns = [
    # pervious
    # path('login/', views.user_login, name='login'),
    # new with login/logout
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.xhtml'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('', views.dashboard, name='dashboard'),
]
