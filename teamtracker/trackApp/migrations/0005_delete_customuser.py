# Generated by Django 4.0.6 on 2022-07-17 13:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trackApp', '0004_rename_users_project_user_customuser'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CustomUser',
        ),
    ]
