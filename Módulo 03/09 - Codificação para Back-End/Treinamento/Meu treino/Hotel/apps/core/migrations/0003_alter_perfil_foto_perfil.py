# Generated by Django 5.0.6 on 2024-05-21 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_rename_foto_de_perfil_perfil_foto_perfil_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfil',
            name='foto_perfil',
            field=models.ImageField(upload_to='fotos_perfil/'),
        ),
    ]
