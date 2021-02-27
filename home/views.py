from django.shortcuts import render, redirect, HttpResponse
from .models import *
from accounts.models import *
from django.contrib import messages

# Create your views here.
def home(request):
    news = News.objects.all()
    category = Categories.objects.all()
    subcategories = SubCategories.objects.all()
    authors = Authors.objects.all()
    links = ImportantLinks.objects.all()
    
    params = {'news': news, 'category':category, 'subcategories':subcategories, 'authors':authors, 'links':links}
    return render(request, 'index.html', params)

def contact(request):
    news = News.objects.all()
    category = Categories.objects.all()
    subcategories = SubCategories.objects.all()
    authors = Authors.objects.all()
    links = ImportantLinks.objects.all()
    
    params = {'news': news, 'category':category, 'subcategories':subcategories, 'authors':authors, 'links':links}
    
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        contact = request.POST['contact']
        message = request.POST['message']
        entry = Contacts(name=name, email=email, contact=contact, message=message)
        entry.save()
        messages.success(request, 'We have recieved your message.')
        return redirect('/contact-us')

    return render(request, 'Contact_us.html', params)
    # return HttpResponse(category)

def SingleNews(request, category, subCategory, singleNewsID):
    singleNews = News.objects.get(id=singleNewsID)
    singleNews.visits = int(singleNews.visits) + 1
    singleNews.save()
    news = News.objects.all()
    category = Categories.objects.all()
    subcategories = SubCategories.objects.all()
    authors = Authors.objects.all()
    links = ImportantLinks.objects.all()
    relatedNews = News.objects.filter(category=singleNews.category).all()
    
    params = {'news': news, 'category':category, 'subcategories':subcategories, 'authors':authors, 'links':links, 'singleNews':singleNews, 'relatedNews':relatedNews}
    return render(request, 'single.html', params)
    # return HttpResponse(relatedNews)

def categoryNews(request, categoryName):
    news = News.objects.all()
    category = Categories.objects.all()
    categoriedd = Categories.objects.get(name=categoryName)
    subcategories = SubCategories.objects.all()
    authors = Authors.objects.all()
    links = ImportantLinks.objects.all()
    categorizedNews = News.objects.filter(category=categoriedd.id)
    
    params = {'news': news, 'category':category, 'subcategories':subcategories, 'authors':authors, 'links':links, 'categorizedNews':categorizedNews, 'categoryName':categoriedd.name}
    return render(request, 'blog.html', params)

def subCategoryNews(request, categoryName, subCategoryName):
    news = News.objects.all()
    category = Categories.objects.all()
    categoriedd = Categories.objects.get(name=categoryName)
    subCategoriedd = SubCategories.objects.get(name=subCategoryName)
    subcategories = SubCategories.objects.all()
    authors = Authors.objects.all()
    links = ImportantLinks.objects.all()
    categorizedNews = News.objects.filter(category=categoriedd.id, subCategory=subCategoriedd.id)
    
    params = {'news': news, 'category':category, 'subcategories':subcategories, 'authors':authors, 'links':links, 'categorizedNews':categorizedNews, 'categoryName':categoriedd.name}
    return render(request, 'blog.html', params)


