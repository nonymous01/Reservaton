# Generated by Django 5.0.4 on 2024-04-21 12:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App_reservation', '0004_alter_auth_email'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Auth',
            new_name='AuthUser',
        ),
    ]