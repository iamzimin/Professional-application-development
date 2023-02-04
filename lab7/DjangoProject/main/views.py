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


# def callHistory(request):
#     ch = CallHistory.objects.all()
#     return render(request, 'main/callHistory.html', {'callHistory': ch})
#
#
# def clientInfo(request):
#     ci = ClientInfo.objects.all()
#     return render(request, 'main/clientInfo.html', {'clientInfo': ci})
#
#
# def clientGroup(request):
#     cg = ClientGroup.objects.all()
#     return render(request, 'main/clientGroup.html', {'clientGroup': cg})
#
#
# def bank(request):
#     b = Bank.objects.all()
#     return render(request, 'main/bank.html', {'bank': b})
#
#
# def bankType(request):
#     bt = BankType.objects.all()
#     return render(request, 'main/bankType.html', {'bankType': bt})


def table_view(request, idx):
    table = []
    names = []
    if idx == 0:
        names = ["id", "ФИО", "Дата", "Текст", "id клиента", "id банка"]
        for m in CallHistory.objects.all():
            table.append([m.id, m.fio, m.date, m.text, m.clientId, m.bankId])

    elif idx == 1:
        names = ["id", "Адрес", "Возраст", "Номер телефона"]
        for m in ClientInfo.objects.all():
            table.append([m.id, m.address, m.age, m.phoneNumber])

    elif idx == 2:
        names = ["id", "Надёжный", "VIP", "Тип клиента"]
        for m in ClientGroup.objects.all():
            table.append([m.id, m.isRelible, m.isVIP, m.type])

    elif idx == 3:
        names = ["id", "Название банка", "Адрес", "Тип банка"]
        for m in Bank.objects.all():
            table.append([m.id, m.bankName, m.address, ", ".join(map(str, m.bankType.all()))])

    elif idx == 4:
        names = ["id", "Тип банка"]
        for m in BankType.objects.all():
            table.append([m.id, m.bankType])

    return render(request, 'main/table_show.html', {'table': table, 'names': names})

