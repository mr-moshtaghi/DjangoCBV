from .models import Todo
from django.views.generic import ListView # __init__.py   __all__
from django.views.generic import DetailView


class Home(ListView): # first/todo_list.html
	template_name = 'first/home.html'
	context_object_name = 'todos' # object_list
	ordering = ['-created']

	def get_queryset(self):
		return Todo.objects.all()


class DetailTodo(DetailView): # first/todo_detail.html  object
	slug_field = 'slug'
	slug_url_kwarg = 'myslug'

	def get_queryset(self, **kwargs):
		if self.request.user.is_authenticated:
			return Todo.objects.filter(slug=self.kwargs['myslug'])
		else:
			return Todo.objects.none()