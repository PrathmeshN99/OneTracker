from django.urls import path
from trackApp import views

urlpatterns = [
    path('',views.login,name='login'),
    path('login',views.login,name='login'),
    path('register',views.register,name='register'),
    path('home',views.home,name='home'),
    path('profile',views.profile,name='profile'),
    path('aboutapp',views.aboutApp,name='aboutapp'),
    path('quickguide',views.quickGuide,name='quickguide'),
    path('logout',views.logout_view,name="logout_view"),
    path('createProject',views.createProject,name="createProject"),
    path('joinProject',views.joinProject,name="joinProject"),
    path('myProjects',views.myProjects,name="myProjects"),
    path('projectDetailsForManager',views.projectDetailsForManager,name="projectDetailsForManager"),
    path('projectDetailsForEmployee',views.projectDetailsForEmployee,name="projectDetailsForEmployee"),   
]
