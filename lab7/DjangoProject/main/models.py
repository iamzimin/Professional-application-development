from django.db import models


class CallHistory(models.Model):
    fio = models.CharField('ФИО', max_length=100)
    date = models.DateTimeField('Дата обращения')
    text = models.CharField('Тип обращения', max_length=300)
    clientId = models.IntegerField('id клиента', default=0)
    # clientId = models.ForeignKey('id клиента', on_delete=models.SET_NULL)#############
    bankId = models.IntegerField('id банка', default=0)

    def __str__(self):
        return self.fio

    class Meta:
        verbose_name = 'История обращений'
        verbose_name_plural = 'История обращений'


class ClientInfo(models.Model):
    address = models.CharField('Адрес', max_length=150)
    age = models.IntegerField('Возраст', default=0)
    phoneNumber = models.IntegerField('Номер телефона', default=0)

    def __str__(self):
        return str(self.phoneNumber)

    class Meta:
        verbose_name = 'Информация о клиенте'
        verbose_name_plural = 'Информация о клиентах'


class ClientGroup(models.Model):
    isRelible = models.BooleanField('Надёжный', default=False)
    isVIP = models.BooleanField('VIP', default=False)
    type = models.CharField('Тип клиента', max_length=50)

    # def __str__(self):
    #     return self.phoneNumber

    class Meta:
        verbose_name = 'Группа клиентов'
        verbose_name_plural = 'Группы клиентов'


class Bank(models.Model):
    bankName = models.CharField('Название банка', max_length=50)
    address = models.CharField('Адрес', max_length=150)
    bankType = models.CharField('Тип банка', max_length=100)

    def __str__(self):
        return self.bankName

    class Meta:
        verbose_name = 'Банк'
        verbose_name_plural = 'Банки'


class BankType(models.Model):
    bankId = models.IntegerField('id банка', default=0)
    bankType = models.CharField('Тип банка', max_length=100)

    # def __str__(self):
    #     return self.bankName

    class Meta:
        verbose_name = 'Тип банка'
        verbose_name_plural = 'Типы банков'
