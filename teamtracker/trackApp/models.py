from django.db import models
from django.contrib.auth.models import User, AbstractUser
from django.contrib.auth import get_user_model

class CustomUser(AbstractUser):
    isLeader = models.BooleanField(default=False)
    isMember = models.BooleanField(default=True)

class Project(models.Model):
    title = models.CharField(max_length=20)
    user = models.ManyToManyField(get_user_model())
    content = models.CharField(max_length=100)
    unique_code = models.CharField(max_length=20)

    def __str__(self):
        return self.title
    