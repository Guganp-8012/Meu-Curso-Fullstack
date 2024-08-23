# Generated by Django 5.0.6 on 2024-05-27 13:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('avaliacao', '0002_remove_feedback_cliente_alter_feedback_avalie'),
        ('core', '0007_perfil_cliente'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback',
            name='cliente',
            field=models.OneToOneField(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.perfil'),
        ),
    ]
