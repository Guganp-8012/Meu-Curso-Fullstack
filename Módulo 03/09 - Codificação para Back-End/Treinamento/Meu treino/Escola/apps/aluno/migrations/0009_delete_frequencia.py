# Generated by Django 5.0.6 on 2024-05-23 11:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aluno', '0008_delete_faltas_remove_frequencia_quantidade_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Frequencia',
        ),
    ]
