# Generated by Django 4.1.3 on 2022-11-16 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0022_remove_post_location2_alter_post_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='description',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
