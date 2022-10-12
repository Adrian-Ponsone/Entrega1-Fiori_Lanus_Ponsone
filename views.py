from unicodedata import name
from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime
from home.models import User2

def user_creation(request):

    name = request.POST.get('name')
    print(name)
    last_name = request.POST.get('last_name')
    print(last_name)

    user = User2(name = name, last_name = last_name, creation_date = datetime.now())
    user.save()

    return render(request, 'home/user_creation.html', {'user' : user})
    
def view_users(request):
    users = User2.objects.all()
    return render(request, 'home/view_users.html', {'users' : users})

def index_bootstrap(request):
    return render(request, 'home/index.html')