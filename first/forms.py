from django import forms
from .models import Comment


class TodoCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'body')


class TodoCreateForm(forms.Form):
    title = forms.CharField(max_length=200)
