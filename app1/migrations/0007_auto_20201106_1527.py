# Generated by Django 3.0.3 on 2020-11-06 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0006_auto_20201106_1524'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='Contactno',
            field=models.IntegerField(default='0'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='RentCost',
            field=models.IntegerField(default='0'),
        ),
    ]
