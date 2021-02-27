from django.shortcuts import render, redirect, HttpResponse
from home.models import *
from .models import *
from django.conf import settings
from django.contrib import messages
from django.contrib import auth
from django.contrib.auth.models import User
import random
from django.core.mail import send_mail
import smtplib, ast
from datetime import datetime


# Create your views here.

def register(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        contact = request.POST.get('contact')
        password = request.POST.get('password')
        cpassword = request.POST.get('cpassword')
        address = request.POST.get('address')

        if (password == cpassword):
            if UserModels.objects.filter(username=email).exists():
                messages.error(request, 'Username or Email already exists. Please select a different username or Email.')
                return redirect('/accounts/register')
            elif UserModelsWithoutOTP.objects.filter(username=email).exists():
                messages.error(request, 'Username or Email already exists. Please select a different username or Email.')
                return redirect('/accounts/register')

            else:
                otp = random.randint(100000, 999999)
                studentsotp = UserModelsWithoutOTP(
                                    name=str(name), contact=contact, 
                                    email=email, username=email, password=password, 
                                    address=address,
                                    otp=otp
                                    )
                studentsotp.save()

                subject = 'Account Confirmation from Imperia Education'
                body = 'Your code for the email confirmation is ' + str(otp) + '. Enter the code in the verification page to verify your ID and activate your account.'
                message = subject + '\n' + body
                email_to = [email]
                
                obj = smtplib.SMTP('smtp.gmail.com', 587)
                obj.starttls()
                obj.login('abiralmahdi@gmail.com', 'Abiralmahdiakhand,2002')
                obj.sendmail('abiralmahdi@gmail.com', email_to, message)
                params = {'username':email}
                return render(request, 'otp.html', params)

        else:
            messages.error(request, 'Your passwords does not match.')

    news = News.objects.all()
    category = Categories.objects.all()
    subcategories = SubCategories.objects.all()
    authors = Authors.objects.all()
    links = ImportantLinks.objects.all()
    
    params = {'news': news, 'category':category, 'subcategories':subcategories, 'authors':authors, 'links':links}

    return render(request, 'signup.html', params)

def confirmRegistration(request, uname):
    if request.method == 'POST':
        code = request.POST.get('otp')

        studentsotp = UserModelsWithoutOTP.objects.get(username=uname)
        if code == studentsotp.otp:

            user = User.objects.create_user(studentsotp.username, studentsotp.email, studentsotp.password)
            user.first_name = studentsotp.name
            user.save()

            user2 = UserModels(
                            name=studentsotp.name, contact=studentsotp.contact, 
                            email=studentsotp.email, username=studentsotp.username, password=studentsotp.password, 
                            address=str(studentsotp.address),    
                            )
            user2.save()

            userall = AllUsers(
                name=studentsotp.name, contact=studentsotp.contact, 
                email=studentsotp.email, username=studentsotp.username, password=studentsotp.password, 
                accounts_type='Visitor'
            )
            userall.save()
            

            messages.success(request, 'You have created your account successfully!')
            
            user = auth.authenticate(username=studentsotp.username, password=studentsotp.password)
            auth.login(request, user)
            studentsotp.delete()
            messages.success(request, 'You have created your account successfully')
            return redirect('/')
        else:
            studentsotp.delete()
            messages.error(request, 'The code does not match your OTP. Please fill up the registration form and submit again.')
            return redirect('/accounts/register')



def authorRegistration(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        contact = request.POST['contact']
        eContact = request.POST['eContact']
        password = request.POST['password']
        confirmPassword = request.POST['confirmPassword']
        address = request.POST['address']
        image = request.POST['image']
        cv = request.POST['cv']
        if password == confirmPassword:
            entry = AuthorsApplied(name=name, email=email, username=email, address=address, password=password, contact1=contact, contact2=eContact)
            entry.save()
            messages.success(request, 'Applied Successfully. We will call you up soon!')
            return redirect('/')
        else:
            messages.error(request, 'Your passwords dont match')
            return redirect('/accounts/authorRegistration')
    return render(request, 'authorRegistration.html')


def authorConfirmation(request, id):
    return redirect('/accounts/adminPanel')

def login(request):
    news = News.objects.all()
    category = Categories.objects.all()
    subcategories = SubCategories.objects.all()
    authors = Authors.objects.all()
    links = ImportantLinks.objects.all()
    
    params = {'news': news, 'category':category, 'subcategories':subcategories, 'authors':authors, 'links':links}

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            messages.success(request, 'Successfully logged in, ' + str(user.username) + '!')
            return redirect('/')
        else:
            messages.error(request, 'Incorrect credentials')
            return redirect('/accounts/login')
    else:    
        return render(request, 'login.html', params)

def logout(request):
    auth.logout(request)
    messages.success(request, 'Successfully logged out!')
    return redirect('/accounts/login')



def userDashboard(request, uname):
    return render(request, 'student-dashboard.html')





def authorDashboard(request, uname):
    return render(request, 'authorDashboard.html')




def send_mail_newsletter(request):
    emails = Newsletter.objects.all()
    email_list = [email.email for email in emails]
    
    if request.method == 'POST':

        subject = request.POST.get('topic')
        body = request.POST.get('desc')
        message = subject + '\n' + body
        email_to = email_list
    
        obj = smtplib.SMTP('smtp.gmail.com', 587)
        obj.starttls()
        obj.login('abiralmahdi@gmail.com', 'Doors.290')
        obj.sendmail('abiralmahdi@gmail.com', email_to, message)
        messages.success(request, 'Your emails have been sent')
        return redirect('/accounts/adminPanel')
    else:
        return render(request, 'newsletter.html')


