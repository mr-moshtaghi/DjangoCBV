from django.db import models
from django.urls import reverse


class Todo(models.Model):
	title = models.CharField(max_length=100)
	created = models.DateTimeField(auto_now_add=True)
	slug = models.SlugField(blank=True, null=True)

	def __str__(self):
		return self.title