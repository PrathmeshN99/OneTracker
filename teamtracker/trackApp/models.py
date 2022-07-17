from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=20)
    user = models.ManyToManyField(get_user_model())
    content = models.CharField(max_length=100)
    unique_code = models.CharField(max_length=20)

    def __str__(self):
        return self.title
    