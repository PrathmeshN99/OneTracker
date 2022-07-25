# Generated by Django 4.0.6 on 2022-07-20 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trackApp', '0010_remove_project_member_project_members_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='manager',
            name='project',
        ),
        migrations.AddField(
            model_name='manager',
            name='project',
            field=models.ManyToManyField(related_name='%(class)s_managerProject', to='trackApp.project'),
        ),
        migrations.RemoveField(
            model_name='member',
            name='project',
        ),
        migrations.AddField(
            model_name='member',
            name='project',
            field=models.ManyToManyField(related_name='%(class)s_memberProject', to='trackApp.project'),
        ),
    ]
