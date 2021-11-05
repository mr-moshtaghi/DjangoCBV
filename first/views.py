from .models import Todo, Comment
from .forms import TodoCommentForm
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView, FormView
from django.views.generic.base import TemplateView, View
from django.views.generic.edit import FormMixin
from django.urls import reverse_lazy, reverse
from django.utils.text import slugify
from django.contrib import messages
from django.views.generic.dates import MonthArchiveView
from django.contrib.auth.mixins import LoginRequiredMixin


class Home(ListView):  # first/todo_list.html
    template_name = 'first/home.html'
    # model = Todo
    # queryset = Todo.objects.all()
    context_object_name = 'todos'  # object_list
    ordering = ['-created']

    def get_queryset(self):
        return Todo.objects.all()


class DetailTodo(LoginRequiredMixin, FormMixin, DetailView):  # first/todo_detail.html  object
    model = Todo
    form_class = TodoCommentForm
    slug_field = 'slug'  # in model
    slug_url_kwarg = 'myslug'  # in path

    # def get_queryset(self, **kwargs):
    # 	if self.request.user.is_authenticated:
    # 		return Todo.objects.filter(slug=self.kwargs['myslug'])
    # 	else:
    # 		return Todo.objects.none()

    def get_success_url(self):
        return reverse('first:detail_todo', kwargs={'myslug': self.object.slug})

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            comment = Comment(todo=self.object, name=form.cleaned_data['name'], body=form.cleaned_data['body'])
            comment.save()
        return super().form_valid(form)


# class TodoCreate(FormView):
# 	form_class = TodoCreateForm
# 	template_name = 'first/todo_create.html'
# 	success_url = reverse_lazy('first:home')
#
# 	def form_valid(self, form):
# 		self.create_todo(form.cleaned_data)
# 		return super().form_valid(form)
#
# 	def create_todo(self, data):
# 		todo = Todo(title=data['title'], slug=slugify(data['title']))
# 		todo.save()
# 		messages.success(self.request, 'your todo add', 'success')


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
