from django.shortcuts import render
from datetime import datetime
from home.models import User

def user_creation(request, name, last_name):
    user = User(name = name, last_name = last_name, creation_date = datetime.now())
    user.save()
    return render(request, 'home/user_creation.html', {'user' : user})
    
def view_users(request):
    users = User.objects.all()
    return render(request, 'home/view_users.html', {'users' : users})

def index_bootstrap(request):
    return render(request, 'home/index.html') 

def about_us(request):
    return render(request,'home/about.html')
