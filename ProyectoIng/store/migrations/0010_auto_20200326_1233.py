# Generated by Django 3.0.3 on 2020-03-26 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0009_auto_20200316_0949'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='store',
            name='store_images',
        ),
        migrations.AddField(
            model_name='store',
            name='store_background_image',
            field=models.ImageField(default='profile_img/default_background.jpg', upload_to='store_background'),
        ),
        migrations.AddField(
            model_name='store',
            name='store_profile_image',
            field=models.ImageField(default='profile_img/default.png', upload_to='store_profile'),
        ),
    ]
