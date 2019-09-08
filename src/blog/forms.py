from django import forms
from .models import Article, Comment

class CommentModelForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = [
            'content',
            'author',
            'id'
        ]