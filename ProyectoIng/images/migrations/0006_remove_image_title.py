# Generated by Django 3.0.3 on 2020-03-15 23:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0005_image_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='title',
        ),
    ]
