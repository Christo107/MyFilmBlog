from .models import Comment, Post, Actor
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)


class BlogForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'


class ActorForm(forms.ModelForm):
    class Meta:
        model = Actor
        fields = '__all__'
