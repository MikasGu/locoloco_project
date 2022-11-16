from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from location_field.models.plain import PlainLocationField


class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Post(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    poster = models.ForeignKey(User, on_delete=models.CASCADE)
    photo = models.ImageField(null=True, blank=True, upload_to='images/', default='images/img.png')

    location = PlainLocationField(zoom=7, default='54.6878,25.2797')

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.photo.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            quality_val = 90
            img.save(self.photo.path, quality=quality_val)

    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        return self.name


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body[0:50]


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.png', upload_to='profile_pics')

    def __str__(self):
        return self.user.username
