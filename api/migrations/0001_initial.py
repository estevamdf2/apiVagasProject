# Generated by Django 2.0 on 2017-12-23 02:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vaga',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=30)),
                ('descricao', models.TextField()),
                ('salario', models.FloatField()),
                ('tipo_contrato', models.CharField(choices=[('PJ', 'Pessoa Juridica'), ('CLT', 'Consolidação das leis do Trabalho')], max_length=50)),
                ('status', models.BooleanField(default=1)),
            ],
        ),
    ]
