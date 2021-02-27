from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('contact-us', views.contact, name='contact'),
    path('news/<str:category>/<str:subCategory>/<str:singleNewsID>', views.SingleNews, name='SingleNews'),
    path('news/<str:categoryName>', views.categoryNews, name='categoryNews'),
    path('news/<str:categoryName>/<str:subCategoryName>', views.subCategoryNews, name='subCategoryNews'),
    
    
    

]
