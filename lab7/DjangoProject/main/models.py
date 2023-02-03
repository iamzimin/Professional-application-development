from django.db import models


class Table1(models.Model):
    fio = models.CharField('ФИО', max_length=100)
    date = models.DateTimeField('Дата обращения')
    text = models.CharField('Тип обращения', max_length=300)
    clientId = models.IntegerField('id клиента', default=0)
    bankId = models.IntegerField('id банка', default=0)

    def __str__(self):
        return self.fio

    class Meta:
        verbose_name = 'История обращений'
        verbose_name_plural = 'История обращений'


class Table2(models.Model):
    fio = models.CharField('ФИО', max_length=100)
    date = models.DateTimeField('Дата обращения')
    text = models.CharField('Тип обращения', max_length=300)
    clientId = models.IntegerField('id клиента', default=0)
    bankId = models.IntegerField('id банка', default=0)

    def __str__(self):
        return self.fio

    class Meta:
        verbose_name = 'История обращений'
        verbose_name_plural = 'История обращений'
