# Generated by Django 4.2.3 on 2023-08-19 05:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sign_in', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customuser',
            old_name='mname',
            new_name='middle_name',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='fname',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='lname',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='mail',
        ),
    ]
