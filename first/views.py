from .models import Todo
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from django.utils.text import slugify
from django.contrib import messages
from django.views.generic.dates import MonthArchiveView
from django.contrib.auth.mixins import LoginRequiredMixin


class Home(ListView): # first/todo_list.html
	template_name = 'first/home.html'
	context_object_name = 'todos' # object_list
	ordering = ['-created']

	def get_queryset(self):
		return Todo.objects.all()


class DetailTodo(LoginRequiredMixin, DetailView): # first/todo_detail.html  object
	model = Todo
	slug_field = 'slug'
	slug_url_kwarg = 'myslug'


class TodoCreate(CreateView):
	model = Todo
	fields = ('title',)
	template_name = 'first/todo_create.html'
	success_url = reverse_lazy('first:home')

	def form_valid(self, form):
		todo = form.save(commit=False)
		todo.slug = slugify(form.cleaned_data['title'])
		todo.save()
		messages.success(self.request, 'your todo added', 'success')
		return super().form_valid(form)

class DeleteTodo(DeleteView):
	model = Todo
	template_name = 'first/todo_delete.html'
	success_url = reverse_lazy('first:home')

class UpdateTodo(UpdateView):
	model = Todo
	fields = ('title',)
	template_name = 'first/update_todo.html'
	success_url = reverse_lazy('first:home')

class MonthTodo(MonthArchiveView):
	model = Todo
	date_field = 'created'
	template_name = 'first/todo_month.html'