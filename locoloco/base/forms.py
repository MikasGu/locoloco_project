from django.forms import ModelForm, HiddenInput
from emoji_picker.widgets import EmojiPickerTextInput

from .models import Post, Comment


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
