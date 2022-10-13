from unicodedata import name
from django.http import HttpResponse
from django.shortcuts import render, redirect
from datetime import datetime
from home.models import User
from home.forms import UserForm, SearchUserForm

def user_creation(request):
    
    if request.method == 'POST':
        
        form =UserForm(request.POST)
        
        if form.is_valid():
            data = form.cleaned_data
            name = data['name']
            last_name = data['last_name']
            registration_date =  data.get('registration_date', datetime.now())
            
            user = User(name = name, last_name = last_name, registration_date = registration_date)
            user.save()
            return redirect('view_users')
    
    form = UserForm()
    return render(request, 'home/user_creation.html', {'form' : form})
    
def view_users(request):
   
    name = request.GET.get('name', None)
    if name:
        users = User.objects.filter(name__icontains=name)
    else:
        users = User.objects.all()
        
    form = SearchUserForm()
    return render(request, 'home/view_users.html', {'users' : users, 'form' : form})

def index_bootstrap(request):
    return render(request, 'home/index.html') 

def about_us(request):
    return render(request,'home/about.html')
