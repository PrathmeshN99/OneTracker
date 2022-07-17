from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib import messages
from .models import Project
import numpy as np

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
            user.save()
            print("Created user " + user_name)
            return redirect('/')
    else:
        return render(request,'register.html')
 
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

@login_required
def home(request):
    return render(request,'home.html')

@login_required
def profile(request):
    # def sample_view(request):
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
        user = request.user
        content = request.POST['content']
        project = Project.objects.create(title=title,user=user,content=content)
        project.save()
        return redirect('/myProjects')
    return render(request,'createProject.html')

def joinProject(request):
    return render(request,'joinProject.html')

def myProjects(request):
        title = Project.objects.filter(user=request.user)[0].title
        context = { 'title' : title }
        return render(request,'myProjects.html',context)

    
