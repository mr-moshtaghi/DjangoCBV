from django.shortcuts import render
from django.contrib.auth import views as auth_views


class UserLogin(auth_views.LoginView):
	template_name = 'accounts/login.html'