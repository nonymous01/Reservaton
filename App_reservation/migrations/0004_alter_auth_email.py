# Generated by Django 5.0.4 on 2024-04-21 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_reservation', '0003_client_nombre_de_personnes_client_toute_demande_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auth',
            name='email',
            field=models.EmailField(default='youssef@gmail.com', max_length=254, unique=True),
        ),
    ]
