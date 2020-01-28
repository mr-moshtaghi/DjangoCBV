from django.shortcuts import render
from django.views.generic.base import TemplateView
from .models import Todo


class Home(TemplateView):
	template_name = 'first/home.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['todos'] = Todo.objects.all()
		return context