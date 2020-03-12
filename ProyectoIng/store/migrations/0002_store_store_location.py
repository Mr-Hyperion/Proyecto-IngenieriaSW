# Generated by Django 3.0.3 on 2020-03-12 03:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('location', '0001_initial'),
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='store',
            name='store_location',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='location.Location'),
            preserve_default=False,
        ),
    ]
