from django.contrib.auth.models import User
from django.forms import ModelForm, HiddenInput
from emoji_picker.widgets import EmojiPickerTextInput
from .models import Post, Comment, Profile


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
        exclude = ['likes']
        widgets = {'poster': HiddenInput(),
                   'name': EmojiPickerTextInput}


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = '__all__'
        widgets = {'post': HiddenInput(),
                   'user': HiddenInput()}
        labels = {
            'body': '',
        }


class ProfileForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
