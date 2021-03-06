# Generated by Django 3.1 on 2022-02-12 16:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0015_auto_20220212_1526'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='allproduct',
            name='id',
        ),
        migrations.AddField(
            model_name='allproduct',
            name='productid',
            field=models.CharField(default='P01', max_length=100, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='orderlist',
            name='productid',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='company.allproduct'),
        ),
    ]
