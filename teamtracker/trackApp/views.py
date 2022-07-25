from unicodedata import name
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib import messages
from .decorators import unauthenticated_user, allowed_users
from .models import Project, Manager, Member
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

# @allowed_users(allowed_roles=['Manager'])
def createProject(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        random_num = np.random.randint(1001,9999) 
        unique_code = str(request.user)[:4] + str(random_num)
        managerUser = request.user 
        project = Project.objects.create(title=title,content=content,unique_code=unique_code)
        if Manager.objects.filter(user=request.user).exists():
            manager = Manager.objects.filter(user=request.user)
            manager[0].project.add(project)
        else:
            managerCreate = Manager.objects.create(user=request.user)
            managerCreate.project.add(project)
            managerCreate.save()
        managers = Manager.objects.filter(project=project)
        for manager in managers:
            project.manager.add(manager.user)
        project.save()
        return redirect('/myProjects')
    return render(request,'createProject.html')

def joinProject(request):
    return render(request,'joinProject.html')

def myProjects(request):
        print(request.user)
        #manager = Manager.objects.filter(user=request.user)
        user = request.user
        
        userId = User.objects.filter(username=user)[0].id
        print(userId)
        projects = Project.objects.filter(manager=userId)
        print(projects)
        memberProjects = Project.objects.filter(members=userId)
        print(memberProjects)
        
        if request.method == 'POST':
            request.session['projectTitle'] = request.POST.get('projectTitle','MyPrj')
            if Manager.objects.filter(user=request.user).exists():
                return redirect('projectDetailsForManager')
            return redirect('projectDetailsForManager')
        else:
            context = { 'projects' : projects , 'memberProjects' : memberProjects}
            return render(request,'myProjects.html',context)

def projectDetailsForManager(request):
    project = Project.objects.filter(title=request.session['projectTitle'])
    print(project) 
     
    context = {'projectTitle':request.session['projectTitle']}
    return render(request,'projectDetailsForManager.html',context)
    
def projectDetailsForEmployee(request):
    context = {'projectTitle':request.session['projectTitle']}
    return render(request,'projectDetailsForEmployee.html',context)



    

    
