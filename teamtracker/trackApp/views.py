from unicodedata import name
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib import messages
from .decorators import unauthenticated_user, allowed_users
from .models import Project
import numpy as np
from django.contrib.auth.models import Group

@unauthenticated_user
def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']   
        last_name = request.POST['last_name']
        user_name = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        
        if User.objects.all().filter(username=user_name).exists():
            print("Username already exists")
            return redirect('/register')

        else:    
            user = User.objects.create_user(username=user_name,first_name=first_name,last_name=last_name,email=email,password=password)
            group = Group.objects.get(name='Member')
            user.groups.add(group)
            user.save()
            print("Created user " + user_name)
            return redirect('/')
    else:
        return render(request,'register.html')

@unauthenticated_user
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)
        print("user : ")
        print(user)
        
        if user is not None:
            auth.login(request,user)
            print("logged in")
            # return render(request,'home.html')
            request.session['username']=username
            return redirect('/home')
        else:

            print("Please enter correct credentials")
            return redirect('/')
    else:
        return render(request,'login.html')

@login_required(login_url='login')
def home(request):
    return render(request,'home.html')

@login_required
@allowed_users(allowed_roles=['Manager'])
def profile(request):
    current_user = request.user
    print(current_user)
    print(type(current_user))
    print(current_user)

    context = {
        'username': current_user.username
    }

    return render(request,'profile.html', context=context)


def quickGuide(request):
    return render(request,'quickguide.html')

def aboutApp(request):
    return render(request,'aboutapp.html')

def logout_view(request):
    logout(request)
    messages.success(request,'Logged out')
    return redirect('/')

def createProject(request):
    if request.method == 'POST':
        title = request.POST['title']
        users = User.objects.filter(username=request.user)[0].id
        content = request.POST['content']
        random_num = np.random.randint(1001,9999) 
        unique_code = str(request.user)[:4] + str(random_num)
        project = Project.objects.create(title=title,content=content,unique_code=unique_code)
        project.user.add(users)
        print(users)
        project.save()
        return redirect('/myProjects')
    return render(request,'createProject.html')

def joinProject(request):
    return render(request,'joinProject.html')

def myProjects(request):
        projects = Project.objects.filter(user=request.user)
        context = { 'projects' : projects }
        return render(request,'myProjects.html',context)

    
