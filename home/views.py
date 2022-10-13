from unicodedata import name
from django.http import HttpResponse
from django.shortcuts import render, redirect
from datetime import datetime
from home.models import User

def user_creation(request):
    
    if request.method == 'POST':
        name = request.POST.get('name')
        last_name = request.POST.get('last_name')
        user = User(name = name, last_name = last_name, registration_date = datetime.now())
        user.save()
        return redirect('view_users')
        
    return render(request, 'home/user_creation.html', {})
    
def view_users(request):
    users = User.objects.all()
    return render(request, 'home/view_users.html', {'users' : users})

def index_bootstrap(request):
    return render(request, 'home/index.html') 

def about_us(request):
    return render(request,'home/about.html')
