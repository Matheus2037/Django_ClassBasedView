# Generated by Django 4.1 on 2024-08-05 02:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_features'),
    ]

    operations = [
        migrations.CreateModel(
            name='Planos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criados', models.DateField(auto_now_add=True, verbose_name='Criação')),
                ('modificado', models.DateField(auto_now=True, verbose_name='Atualização')),
                ('ativo', models.BooleanField(default=True, verbose_name='Ativo?')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome')),
                ('valor', models.FloatField(verbose_name='Valor')),
                ('usuario', models.CharField(max_length=100, verbose_name='Usuários')),
                ('capacidade', models.CharField(max_length=100, verbose_name='Capacidade')),
                ('suporte', models.CharField(max_length=100, verbose_name='Suporte')),
                ('atualizacoes', models.CharField(max_length=100, verbose_name='Atualizações')),
            ],
            options={
                'verbose_name': 'Plano',
                'verbose_name_plural': 'Planos',
            },
        ),
    ]