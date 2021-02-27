from django.contrib import admin
from .models import*
from django.apps import apps

#  Register your models here
app2 = apps.get_app_config('accounts')


for model_name, model in app2.models.items():
    admin.site.register(model)