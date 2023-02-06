from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django import forms

# TODO мб нужно на английском
class CallHistoryForm(ModelForm):
    class Meta:
        model = CallHistory
        # fields = ["ФИО", "Дата", "Текст", "id клиента", "id банка"]
        fields = ["fio", "date", "text", "clientId", "bankId"]

    @staticmethod
    def clone(request):
        return CallHistoryForm(request)

    @staticmethod
    def clone_for_edit(istans):
        return CallHistoryForm(instance=istans)


class ClientInfoForm(ModelForm):
    class Meta:
        model = ClientInfo
        # fields = ["Адрес", "Возраст", "Номер телефона"]
        fields = ["address", "age", "phoneNumber", "clientId"]

    @staticmethod
    def clone(request):
        return ClientInfoForm(request)

    @staticmethod
    def clone_for_edit(istans):
        return ClientInfoForm(instance=istans)


class ClientGroupForm(ModelForm):
    class Meta:
        model = ClientGroup
        # fields = ["Надёжный", "VIP", "Тип клиента"]
        fields = ["isRelible", "isVIP", "type"]

    @staticmethod
    def clone(request):
        return ClientGroupForm(request)

    @staticmethod
    def clone_for_edit(istans):
        return ClientGroupForm(instance=istans)


class BankForm(ModelForm):
    class Meta:
        model = Bank
        # fields = ["Название банка", "Адрес", "Тип банка"]
        fields = ["bankName", "address", "bankType"]

    @staticmethod
    def clone(request):
        return BankForm(request)

    @staticmethod
    def clone_for_edit(istans):
        return BankForm(instance=istans)


class BankTypeForm(ModelForm):
    class Meta:
        model = BankType
        # fields = ["Тип банка"]
        fields = ["bankType"]

    @staticmethod
    def clone(request):
        return BankTypeForm(request)

    @staticmethod
    def clone_for_edit(istans):
        return BankTypeForm(instance=istans)


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

