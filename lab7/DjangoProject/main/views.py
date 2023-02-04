from django.shortcuts import render
from .models import CallHistory
from .models import ClientInfo
from .models import ClientGroup
from .models import Bank
from .models import BankType

def index(request):
    return render(request, 'main/index.html')


def main(request):
    data = {
        'title': 'Что это такое?'
    }
    return render(request, 'main/main.html', data)


def table_view(request, idx):
    table = []
    names = []
    if idx == 0:
        names = ["id", "ФИО", "Дата", "Текст", "id клиента", "id банка"]
        for m in CallHistory.objects.all():
            table.append({"id": m.id, 0: m.fio, 1: m.date, 2: m.text, 3: m.clientId, 4: m.bankId})

    elif idx == 1:
        names = ["id", "Адрес", "Возраст", "Номер телефона"]
        for m in ClientInfo.objects.all():
            table.append({"id": m.id, 0: m.address, 1: m.age, 2: m.phoneNumber})

    elif idx == 2:
        names = ["id", "Надёжный", "VIP", "Тип клиента"]
        for m in ClientGroup.objects.all():
            table.append({"id": m.id, 0: m.isRelible, 1: m.isVIP, 2: m.type})

    elif idx == 3:
        names = ["id", "Название банка", "Адрес", "Тип банка"]
        for m in Bank.objects.all():
            table.append({"id": m.id, 0: m.bankName, 1: m.address, 3: ", ".join(map(str, m.bankType.all()))})

    elif idx == 4:
        names = ["id", "Тип банка"]
        for m in BankType.objects.all():
            table.append({"id": m.id, 0: m.bankType})

    return render(request, 'main/table_show.html', {'table_id': idx, 'table': table, 'names': names})

def table_change(request, idx, el, command):
    pass