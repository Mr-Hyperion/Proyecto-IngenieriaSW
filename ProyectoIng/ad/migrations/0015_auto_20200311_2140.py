# Generated by Django 3.0.3 on 2020-03-12 03:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('location', '0001_initial'),
        ('ad', '0014_currencyconversion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ad',
            name='id_location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='location.Location'),
        ),
        migrations.DeleteModel(
            name='Location',
        ),
    ]
