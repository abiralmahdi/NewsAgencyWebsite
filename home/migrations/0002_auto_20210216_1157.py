# Generated by Django 3.0.8 on 2021-02-16 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='categories',
            name='slug',
            field=models.CharField(default='', max_length=1000),
        ),
        migrations.AddField(
            model_name='subcategories',
            name='slug',
            field=models.CharField(default='', max_length=1000),
        ),
    ]
