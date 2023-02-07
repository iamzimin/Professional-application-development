from django.db import models


class CallHistory(models.Model):
    fio = models.CharField('ФИО', max_length=100)
    date = models.DateTimeField('Дата обращения')
    text = models.CharField('Тип обращения', max_length=300)
    clientId = models.ForeignKey('ClientInfo', on_delete=models.CASCADE)##################
    bankId = models.ForeignKey('Bank', on_delete=models.CASCADE)##########################

    names = ["id", "ФИО", "Дата", "Текст", "id клиента", "id банка"]

    def __str__(self):
        return self.fio

    class Meta:
        verbose_name = 'История обращений'
        verbose_name_plural = 'История обращений'


class ClientInfo(models.Model):
    address = models.CharField('Адрес', max_length=150)
    age = models.IntegerField('Возраст', default=0)
    phoneNumber = models.IntegerField('Номер телефона', default=0)
    clientId = models.OneToOneField('ClientGroup', on_delete=models.CASCADE)

    names = ["id", "Адрес", "Возраст", "Номер телефона", "id клиента"]

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = 'Информация о клиенте'
        verbose_name_plural = 'Информация о клиентах'


class ClientGroup(models.Model):
    isRelible = models.BooleanField('Надёжный', default=False)
    isVIP = models.BooleanField('VIP', default=False)
    type = models.CharField('Тип клиента', max_length=50)

    names = ["id", "Надёжный", "VIP", "Тип клиента"]

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = 'Группа клиентов'
        verbose_name_plural = 'Группы клиентов'


class Bank(models.Model):
    bankName = models.CharField('Название банка', max_length=50)
    address = models.CharField('Адрес', max_length=150)
    bankType = models.ManyToManyField('BankType')############################

    names = ["id", "Название банка", "Адрес", "Тип банка"]

    def __str__(self):
        return self.bankName

    class Meta:
        verbose_name = 'Банк'
        verbose_name_plural = 'Банки'


class BankType(models.Model):
    bankType = models.CharField('Тип банка', max_length=100)

    names = ["id", "Тип банка"]

    def __str__(self):
        return self.bankType

    class Meta:
        verbose_name = 'Тип банка'
        verbose_name_plural = 'Типы банков'


# class User(models.Model):
#     login = models.CharField(max_length=150, default="")
#     password = models.CharField(max_length=150, default="")
#     role = models.CharField(max_length=150, default="client")
#
#     names = ["Индекс", "Логин", "Пароль", "Роль"]
#     title = "Пользователи"
#
#     class Meta:
#         verbose_name = 'Тип банка'
#         verbose_name_plural = 'Типы банков'
#
#
#     def __str__(self):
#         return str(self.login)
#
