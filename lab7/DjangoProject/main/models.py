from django.db import models


class Table1(models.Model):
    fio = models.CharField('ФИО', max_length=100)
    date = models.DateTimeField('Дата обращения')
    text = models.CharField('Тип обращения', max_length=300)

    def __str__(self):
        return self.fio

    class Meta:
        verbose_name = 'Таблица 1'
        verbose_name_plural = 'Таблицы 1'
