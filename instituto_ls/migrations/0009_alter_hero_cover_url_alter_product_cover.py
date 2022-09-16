# Generated by Django 4.1.1 on 2022-09-16 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instituto_ls', '0008_hero_cover_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hero',
            name='cover_url',
            field=models.URLField(blank=True, max_length=5000, null=True, verbose_name='URL da imagem'),
        ),
        migrations.AlterField(
            model_name='product',
            name='cover',
            field=models.ImageField(upload_to='products', verbose_name='Imagem'),
        ),
    ]
