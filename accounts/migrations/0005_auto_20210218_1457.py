# Generated by Django 3.0.8 on 2021-02-18 08:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0004_allusers'),
    ]

    operations = [
        migrations.AddField(
            model_name='authors',
            name='date_of_apply',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='AuthorsApplied',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=1000)),
                ('username', models.CharField(max_length=1000)),
                ('contact1', models.CharField(max_length=1000)),
                ('contact2', models.CharField(max_length=5000)),
                ('address', models.CharField(max_length=5000)),
                ('pay', models.CharField(max_length=5000)),
                ('password', models.CharField(max_length=5000)),
                ('image', models.ImageField(upload_to='images')),
                ('date_of_apply', models.DateField(auto_now_add=True)),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
