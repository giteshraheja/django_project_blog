from django_summernote.widgets import SummernoteWidget
from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content')
        widgets = {
            'content': SummernoteWidget(),
        }
