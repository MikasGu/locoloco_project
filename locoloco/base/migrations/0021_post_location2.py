# Generated by Django 4.1.3 on 2022-11-16 12:15

from django.db import migrations
import mapbox_location_field.models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0020_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='location2',
            field=mapbox_location_field.models.LocationField(default=(23, 23), map_attrs={}),
            preserve_default=False,
        ),
    ]