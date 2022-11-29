from django.contrib.auth.models import User
from django.forms import ModelForm, HiddenInput, TextInput, Select, ClearableFileInput
from mapbox_location_field.widgets import MapInput

from .models import Post, Comment, Profile


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
        exclude = ['likes']
        widgets = {
            'poster': HiddenInput(),
            'name': TextInput(attrs={
                'placeholder': 'Name',
                'class': 'form-control rounded-pill mb-2'}),
            'category': Select(attrs={
                'class': 'form-control rounded-pill',
            }),
            'photo': ClearableFileInput(attrs={
                'class': 'form-control rounded-pill',
            }),
            'location': MapInput(),
            'description': TextInput(attrs={
                'placeholder': 'Description',
                'class': 'form-control rounded-pill mb-2'
            })}
        labels = {
            'name': '',
            'description': '',
            'category': '',
            'photo': '',
        }


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = '__all__'
        widgets = {'post': HiddenInput(),
                   'user': HiddenInput(),
                   'body': TextInput(attrs={
                       'placeholder': 'Comment',
                       'class': 'form-control rounded-pill mb-2'}),
                   }
        labels = {
            'body': '',
        }


class ProfileForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']


class ProfilePictureForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['image']

