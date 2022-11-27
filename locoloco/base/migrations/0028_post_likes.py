# Generated by Django 4.1.3 on 2022-11-20 20:09

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('base', '0027_alter_comment_body_alter_post_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='collected_votes', to=settings.AUTH_USER_MODEL),
        ),
    ]
