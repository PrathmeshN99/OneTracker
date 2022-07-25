# Generated by Django 4.0.6 on 2022-07-20 14:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('trackApp', '0005_delete_customuser'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='user',
        ),
        migrations.AddField(
            model_name='project',
            name='manager',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
