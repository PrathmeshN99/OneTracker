# Generated by Django 4.0.6 on 2022-07-17 11:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trackApp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='name',
            new_name='title',
        ),
    ]
