# Generated by Django 4.1.2 on 2022-10-13 01:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_alter_usuario_fechanacimiento'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mascota',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('genero', models.CharField(max_length=200)),
                ('tipo', models.CharField(max_length=200)),
                ('raza', models.CharField(max_length=200)),
                ('personalidad', models.CharField(max_length=200)),
                ('edad', models.CharField(max_length=200)),
                ('tamaño', models.CharField(max_length=200)),
                ('ubicacion', models.CharField(max_length=200)),
                ('historial', models.TextField()),
                ('foto', models.CharField(max_length=200)),
                ('video', models.CharField(max_length=200)),
            ],
        ),
    ]
