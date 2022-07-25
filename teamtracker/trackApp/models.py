from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model


class Project(models.Model):
    title = models.CharField(max_length=20)
    manager = models.ManyToManyField(User,related_name="%(class)s_projectManager")
    members = models.ManyToManyField(User,related_name="%(class)s_projectMember")
    content = models.CharField(max_length=100)
    unique_code = models.CharField(max_length=20)

    def __str__(self):
        return self.title


class Manager(models.Model):
    user = models.ForeignKey(User,on_delete=models.SET_NULL,null=True,related_name="%(class)s_manager")
    project = models.ManyToManyField(Project,related_name="%(class)s_managerProject")

    # def __str__(self):
    #     return self.user

class Member(models.Model):
    user = models.ForeignKey(Project,on_delete=models.SET_NULL,null=True,related_name="%(class)s_member")
    project = models.ManyToManyField(Project,related_name="%(class)s_memberProject")

    # def __str__(self):
    #     return self.user