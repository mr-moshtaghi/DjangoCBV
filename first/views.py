from .models import Todo
from django.views.generic.list import ListView


class Home(ListView): # first/todo_list.html
	template_name = 'first/home.html'
	context_object_name = 'todos'
	ordering = ['-created']

	def get_queryset(self):
		return Todo.objects.all()

