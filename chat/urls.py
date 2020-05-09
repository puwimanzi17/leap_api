# account/urls.py
from django.urls import include, path

from . import views
from django.contrib.auth import views as auth_view
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register', views.register, name="signup"),
    path('login', views.post_login, name="login"),
    # path('login', auth_views.LoginView.as_view(), name='login'),
    path('logout', auth_view.LogoutView.as_view(), name="logout"),
    path('send/', views.send_message, name="send"),
    path('post/', views.send_contact, name="post"),
    path('sub/', views.subscribe, name="subscribe"),
]
