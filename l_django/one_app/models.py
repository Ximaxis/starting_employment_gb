from django.db import models


class Item(models.Model):
    title = models.CharField(verbose_name='Название товара', max_length=255)
    price = models.PositiveIntegerField(verbose_name='Цена', default=0)
    vendor = models.CharField(verbose_name='Поставщик', max_length=255)
    create_at = models.DateTimeField(verbose_name='Дата добавления', auto_created=True, auto_now_add=True)

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = u'Карточка товара'
        verbose_name_plural = u'Карточки товаров'
