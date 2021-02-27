from django.db import models
from django.contrib.auth.models import User
from accounts import models as AccountsModels

# Create your models here.
class Contacts(models.Model):
    name = models.CharField(max_length=1000)
    email = models.CharField(max_length=1000)
    contact = models.CharField(max_length=1000)
    message = models.CharField(max_length=1000)

    def __str__(self):
        return self.name

class Categories(models.Model):
    name = models.CharField(max_length=1000)
    image = models.ImageField(upload_to='images')
    slug = models.CharField(max_length=1000, default='')

    def __str__(self):
        return self.name

class SubCategories(models.Model):
    name = models.CharField(max_length=1000)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE,)
    image = models.ImageField(upload_to='images')
    slug = models.CharField(max_length=1000, default='')

    def __str__(self):
        return self.name

class News(models.Model):
    name = models.CharField(max_length=1000)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    subCategory = models.ForeignKey(SubCategories, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE,)
    image = models.ImageField(upload_to='images')
    description = models.CharField(max_length=9999999999999)
    place = models.CharField(max_length=5000)
    date = models.DateField(auto_now_add=True, auto_now=False, blank=True)
    visits = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-visits']

class ImportantLinks(models.Model):
    name = models.CharField(max_length=1000)
    link = models.CharField(max_length=100000)
    slug = models.CharField(max_length=1000)
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.name
