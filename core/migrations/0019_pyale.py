# Generated by Django 2.1.4 on 2019-01-17 21:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0018_pyale'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='active_user',
            new_name='is_active',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='staff_user',
            new_name='is_staff',
        ),
    ]
