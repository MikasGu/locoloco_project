from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from mapbox_location_field.models import LocationField



class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Post(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100, null=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    poster = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, blank=True, related_name="collected_votes")
    photo = models.ImageField(null=True, blank=True, upload_to='images/', default='images/img.png')
    location = LocationField(map_attrs={'center': [25.2797, 54.6872],
                                        'marker_color': "orange",
                                        'readonly': False,
                                        'style': "mapbox://styles/mapbox/dark-v10"})

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.photo.path)

        if img.height > 557 or img.width > 418:
            output_size = (418, 557)
            img.thumbnail(output_size)
            quality_val = 99
            img.save(self.photo.path, quality=quality_val)

    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        return self.name


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.CharField(max_length=100)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body[0:50]


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.png', upload_to='profile_pics')

    def __str__(self):
        return self.user.username
