# Generated by Django 3.0.3 on 2020-11-06 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0005_auto_20201106_1507'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='Contactno',
            field=models.IntegerField(default=' '),
        ),
        migrations.AlterField(
            model_name='profile',
            name='RentCost',
            field=models.IntegerField(default=' '),
        ),
    ]
