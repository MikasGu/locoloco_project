from django.forms import ModelForm, HiddenInput
from .models import Post, Comment
from location_field.forms.plain import PlainLocationField


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
        widgets = {
            'location': PlainLocationField(),
        }


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = '__all__'
        widgets = {'post': HiddenInput(), 'user': HiddenInput()}
