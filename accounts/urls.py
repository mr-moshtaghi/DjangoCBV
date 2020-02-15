from django.urls import path
from django.contrib.auth import views as auth_views
from . import views


app_name = 'accounts'
urlpatterns = [
	path('login/', views.UserLogin.as_view(), name='login'),
	path('logout/', auth_views.LogoutView.as_view(), name='logout'),
	path('reset/', views.UserPassReset.as_view(), name='reset_pass'),
	path('reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='accounts/reset_done.html'), name='password_reset_done'),
]