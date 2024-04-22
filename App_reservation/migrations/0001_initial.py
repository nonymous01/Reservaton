# Generated by Django 5.0.4 on 2024-04-21 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('prenom', models.CharField(max_length=100)),
                ('ncni', models.CharField(max_length=100)),
                ('email', models.EmailField(default='youssef@gmail.com', max_length=254)),
                ('alergie', models.CharField(blank=True, choices=[('alimentaires', 'Alimentaires'), ('animal', 'Animal')], max_length=20)),
                ('Toute_demande', models.CharField(max_length=500)),
                ('telephone', models.CharField(max_length=100)),
                ('Nombre_de_personnes', models.IntegerField()),
                ('status', models.BooleanField(default=False)),
            ],
        ),
    ]