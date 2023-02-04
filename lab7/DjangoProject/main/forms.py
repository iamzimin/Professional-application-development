from django.forms import ModelForm
from .models import *

# TODO мб нужно на английском
class CallHistoryForm(ModelForm):
    class Meta:
        model = CallHistory
        # fields = ["ФИО", "Дата", "Текст", "id клиента", "id банка"]
        fields = ["fio", "date", "text", "clientId", "bankId"]


class ClientInfoForm(ModelForm):
    class Meta:
        model = ClientInfo
        # fields = ["Адрес", "Возраст", "Номер телефона"]
        fields = ["address", "age", "phoneNumber"]


class ClientGroupForm(ModelForm):
    class Meta:
        model = ClientGroup
        # fields = ["Надёжный", "VIP", "Тип клиента"]
        fields = ["isRelible", "isVIP", "type"]


class BankForm(ModelForm):
    class Meta:
        model = Bank
        # fields = ["Название банка", "Адрес", "Тип банка"]
        fields = ["bankName", "address", "bankType"]


class BankTypeForm(ModelForm):
    class Meta:
        model = BankType
        # fields = ["Тип банка"]
        fields = ["bankType"]
