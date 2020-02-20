from django import forms
from .models import Comment

class TodoCommentForm(forms.ModelForm):
	class Meta:
		model = Comment
		fields = ('name', 'body')