# Generated by Django 4.1.1 on 2022-09-13 23:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cover', models.URLField(verbose_name='URL da imagem')),
                ('title', models.CharField(max_length=60, verbose_name='Título')),
                ('description', models.CharField(max_length=95, verbose_name='Descrição')),
                ('know_more', models.TextField(max_length=2000, verbose_name='Saiba mais')),
                ('index', models.IntegerField()),
            ],
            options={
                'verbose_name_plural': 'Produtos',
                'ordering': ['-index'],
            },
        ),
    ]