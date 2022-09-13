from re import T
from django.db import models


class Product(models.Model):
    cover = models.URLField(verbose_name="URL da imagem")
    title = models.CharField(verbose_name='Título', max_length=60)
    description = models.CharField(verbose_name='Descrição', max_length=95)
    know_more = models.TextField(verbose_name='Saiba mais', max_length=2000)
    index = models.IntegerField()

    class Meta:
        ordering = ['-index']
        verbose_name_plural = "Produtos"

    def __str__(self) -> str:
        return self.description

class Hero(models.Model):
    name = models.CharField(verbose_name='Nome', max_length=80)
    cover = models.URLField(verbose_name="Foto (fundo transparente)")
    bio = models.TextField(verbose_name='Biografia suscinta', max_length=150)


class Feedback(models.Model):
    video_iframe = models.TextField(verbose_name='iFrame de Video', blank=True, null=True)
    image_iframe = models.TextField(verbose_name='iFrame de Imagem', blank=True, null=True)
    index = models.IntegerField()

    class Meta:
        ordering = ['-index']




