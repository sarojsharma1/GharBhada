# Generated by Django 3.0.3 on 2020-11-06 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='Uploadimage',
            field=models.ImageField(blank=True, upload_to='images'),
        ),
    ]