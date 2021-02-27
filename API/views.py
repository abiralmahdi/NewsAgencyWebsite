from django.shortcuts import render, HttpResponse
from home.models import *
import json
from django.core import serializers


# Create your views here.
# def api(request, instance):
#     json_object = serializers.serialize("json", News.objects.all())

#     return HttpResponse(json_object)

def api(request, instance):
    instance2 = int(instance)*int(instance)
    dictionary = {
        'name': 'Abir',
        'someData':{
            'email': 'abiralmahdi@gmail.com',
            'contact': '01769025257',
        },
        'value': instance2
    }

    json_object = json.dumps(dictionary, indent = 4)   
    return HttpResponse(json_object)

