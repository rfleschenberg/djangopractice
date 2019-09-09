from django import forms
from .models import Article, Comment

class CommentModelForm(forms.ModelForm):
    content = forms.CharField(
        label='',
        widget=forms.Textarea(
            attrs={
                'rows': 7,
                'cols': 50
            }
        )
    )
    author = forms.CharField(
        label='',
        widget=forms.TextInput(attrs={'placeholder': 'Author'})
    )

    class Meta:
        model = Comment
        fields = [
            'content',
            'author',
        ]