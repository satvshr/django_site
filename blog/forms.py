from django import forms

from .models import Post, Comment

class PostForm(forms.ModelForm):
    #We need to tell Django that this form is a ModelForm forms.ModelForm is responsible for that.

    class Meta:
        model = Post
        fields = ('title', 'text',)

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('title', 'text',)

