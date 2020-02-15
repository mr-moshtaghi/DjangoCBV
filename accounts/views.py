from django.shortcuts import render
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy


class UserLogin(auth_views.LoginView):
	template_name = 'accounts/login.html'

class UserPassReset(auth_views.PasswordResetView):
	template_name = 'accounts/password_reset_form.html'
	success_url = reverse_lazy('accounts:password_reset_done')
	html_email_template_name = 'accounts/password_reset_email.html'