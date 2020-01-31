from django.urls import path
from . import views


app_name = 'first'
urlpatterns = [
	path('', views.Home.as_view(), name='home'),
	path('<slug:myslug>/', views.DetailTodo.as_view(), name='detail_todo')
]