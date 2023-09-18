from .models import Comment, Post
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)


class BlogForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
