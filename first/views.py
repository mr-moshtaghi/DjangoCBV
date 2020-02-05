from .models import Todo
from django.views.generic import ListView # __init__.py   __all__
from django.views.generic import DetailView
from django.views.generic import FormView
from .forms import TodoCreateForm
from django.urls import reverse_lazy
from django.utils.text import slugify
from django.contrib import messages



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


class TodoCreate(FormView):
	form_class = TodoCreateForm
	template_name = 'first/todo_create.html'
	success_url = reverse_lazy('first:home')

	def form_valid(self, form):
		self.create_todo(form.cleaned_data)
		return super().form_valid(form)

	def create_todo(self, data):
		todo = Todo(title=data['title'], slug=slugify(data['title']))
		todo.save()
		messages.success(self.request, 'your todo added', 'success')