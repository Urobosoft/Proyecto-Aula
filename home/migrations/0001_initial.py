# Generated by Django 4.2.6 on 2023-10-19 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=45)),
                ('Edad', models.IntegerField()),
                ('Genero', models.CharField(max_length=10)),
                ('Preferencias_Contenido', models.CharField(max_length=45)),
                ('Correo_Electronico', models.EmailField(max_length=254)),
                ('Password', models.CharField(max_length=45)),
            ],
        ),
    ]
