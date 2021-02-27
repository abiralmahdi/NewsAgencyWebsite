from django.db import models
from django.contrib.auth.models import User
from home import models as homeModel

# Create your models here.
class UserModels(models.Model):
    name = models.CharField(max_length=1000)
    email = models.CharField(max_length=1000)
    username = models.CharField(max_length=1000) # Same As email
    contact = models.CharField(max_length=1000)
    address = models.CharField(max_length=5000)
    password = models.CharField(max_length=5000)

    def __str__(self):
        return self.username

class UserModelsWithoutOTP(models.Model):
    name = models.CharField(max_length=1000)
    email = models.CharField(max_length=1000)
    username = models.CharField(max_length=1000) # Same As email
    contact = models.CharField(max_length=1000)
    address = models.CharField(max_length=5000)
    password = models.CharField(max_length=5000)
    otp = models.CharField(max_length=10000, default='')

    def __str__(self):
        return self.username

class Authors(models.Model):
    name = models.CharField(max_length=1000)
    email = models.CharField(max_length=1000)
    username = models.CharField(max_length=1000) # Same As email
    contact = models.CharField(max_length=1000)
    emergencyContact = models.CharField(max_length=5000)
    address = models.CharField(max_length=5000)
    pay = models.CharField(max_length=5000)
    password = models.CharField(max_length=5000)
    image = models.ImageField(upload_to='images')
    date_of_apply = models.DateField(auto_now_add=True, auto_now=False, blank=True,)


    def __str__(self):
        return self.username


class AuthorsApplied(models.Model):
    name = models.CharField(max_length=2000)
    email = models.CharField(max_length=1000)
    username = models.CharField(max_length=1000) # Same As email
    contact1 = models.CharField(max_length=1000)
    contact2 = models.CharField(max_length=5000)
    address = models.CharField(max_length=5000)
    password = models.CharField(max_length=5000)
    image = models.ImageField(upload_to='images')
    date_of_apply = models.DateField(auto_now_add=True, auto_now=False, blank=True)

    def __str__(self):
        return self.username



class AllUsers(models.Model):
    name = models.CharField(max_length=5000)
    contact = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    accounts_type = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

    def __str__(self):
        return str(self.name) + ' || ' + str(self.email) + ' || ' + str(self.username) + ' || '


