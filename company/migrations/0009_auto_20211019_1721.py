# Generated by Django 3.0 on 2021-10-19 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0008_profile_cartquan'),
    ]

    operations = [
        migrations.AlterField(
            model_name='allproduct',
            name='image',
            field=models.ImageField(blank=True, default='default-image.png', null=True, upload_to='products'),
        ),
    ]