# Generated by Django 4.0.6 on 2022-07-20 17:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('trackApp', '0011_remove_manager_project_manager_project_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='manager',
            name='project',
        ),
        migrations.AddField(
            model_name='manager',
            name='project',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(class)s_managerProject', to='trackApp.project'),
        ),
        migrations.RemoveField(
            model_name='member',
            name='project',
        ),
        migrations.AddField(
            model_name='member',
            name='project',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(class)s_memberProject', to='trackApp.project'),
        ),
    ]
