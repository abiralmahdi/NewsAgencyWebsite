# Generated by Django 3.0.8 on 2021-02-18 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_auto_20210218_2059'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermodels',
            name='name',
            field=models.CharField(max_length=1000),
        ),
    ]