# Generated by Django 5.0.6 on 2024-05-22 13:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aluno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('foto', models.ImageField(upload_to='fotos_perfil/')),
            ],
        ),
        migrations.CreateModel(
            name='DadosPessoais',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sexo', models.CharField(choices=[('M', 'Masculino'), ('F', 'Feminino')], max_length=2)),
                ('nascimento', models.DateField()),
                ('cpf', models.PositiveIntegerField()),
                ('rg', models.PositiveIntegerField()),
                ('historico_escolar', models.FileField(upload_to='doc_aluno/')),
                ('aluno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aluno.aluno')),
            ],
        ),
        migrations.CreateModel(
            name='Frequencia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(choices=[('F', 'Número de Faltas'), ('J', 'Faltas Justificadas'), ('P', 'Dias de Presença')], max_length=3)),
                ('quantidade', models.PositiveIntegerField()),
                ('aluno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aluno.aluno')),
            ],
        ),
    ]
