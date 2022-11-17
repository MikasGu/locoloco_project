from django.forms import ModelForm, HiddenInput
from .models import Post, Comment


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
        widgets = {'poster': HiddenInput()}


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = '__all__'
        widgets = {'post': HiddenInput(), 'user': HiddenInput()}
