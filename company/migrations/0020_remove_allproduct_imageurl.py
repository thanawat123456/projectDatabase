# Generated by Django 3.1 on 2022-03-25 22:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0019_auto_20220325_2200'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='allproduct',
            name='imageurl',
        ),
    ]