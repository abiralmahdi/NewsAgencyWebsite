from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('authorRegistration', views.authorRegistration, name='authorRegister'),
    path('logout', views.logout, name='logout'),
    path('send_mail_newsletter', views.send_mail_newsletter, name='send_mail_newsletter'),
    path('confirmRegistration/<str:uname>', views.confirmRegistration, name='confirmRegistration'),
    path('authorConfirmation/<str:id>', views.authorRegistration, name='authorConfirmation'),
    path('userDashboard/<str:uname>', views.userDashboard, name='userDashboard'),
    path('authorDashboard/<str:uname>', views.authorDashboard, name='authorDashboard'),

    
] 
