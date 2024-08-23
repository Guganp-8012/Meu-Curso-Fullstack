# Generated by Django 5.0.6 on 2024-05-21 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservas', '0006_remove_refeicao_inclui_ref_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='DetalhesAdicionais',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('preferencias', models.CharField(max_length=254)),
                ('condicao_especial', models.CharField(default='adicione aqui informações caso a pessoa necessita de algum tratamento mais delicado ou possui alguma deficiência.', max_length=254)),
            ],
        ),
        migrations.DeleteModel(
            name='DocPagamento',
        ),
        migrations.AlterModelOptions(
            name='refeicao',
            options={'verbose_name': 'Refeição', 'verbose_name_plural': 'Refeições'},
        ),
        migrations.AlterField(
            model_name='refeicao',
            name='valor_ref',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
    ]
